/* ================================================================
   CardShield – ATM Card Fraud Detection
   JavaScript Application Logic
   ================================================================ */

'use strict';

// ─────────────────────────────────────────────────────────────
// Dataset-Derived Constants (from Bank Transaction Dataset)
// ─────────────────────────────────────────────────────────────
const FRAUD_STATS = {
  totalTransactions: 3000000,
  totalFraud: 14954,
  fraudRate: 0.005,        // 0.5% overall fraud rate
  avgFraudAmount: 1833.50,
  avgLegitAmount: 1850.45,

  // Fraud rates by merchant category (from real data analysis)
  categoryFraudRate: {
    'ATM Withdrawal': 0.523, 'Dining': 0.493, 'Education': 0.483,
    'Entertainment': 0.513, 'Fuel': 0.502, 'Fund Transfer': 0.496,
    'Groceries': 0.498, 'Healthcare': 0.521, 'Insurance': 0.478,
    'Rent': 0.489, 'Salary Credit': 0.520, 'Shopping': 0.489,
    'Travel': 0.478, 'Utilities': 0.498
  },

  // Card type distribution
  cardDistribution: {
    'Debit': 35700, 'Credit - Classic': 16300,
    'Credit - Gold': 8367, 'Credit - Platinum': 4633
  },

  // Fraud rate by amount range
  amountFraudRate: {
    'Under \u20b9500': 0.50, '\u20b9500\u20132,000': 0.50,
    '\u20b92,000\u20135,000': 0.49, 'Over \u20b95,000': 0.48
  }
};

// Risk factor weights (sum = 100)
const WEIGHTS = {
  cardStatus: 25,     // Blocked/expired = instant high risk
  amount: 20,         // High amount vs avg
  time: 15,           // Off-hours transactions
  location: 15,       // International = higher risk
  category: 10,       // Category-specific rates
  frequency: 10,      // High transaction frequency
  creditUtil: 5       // Credit limit vs amount ratio
};

// ─────────────────────────────────────────────────────────────
// History Storage
// ─────────────────────────────────────────────────────────────
var analysisHistory = [];
var analysisCount = 0;

// ─────────────────────────────────────────────────────────────
// DOM Ready
// ─────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', function() {
  initParticles();
  initNavbar();
  initCounters();
  initRangeSlider();
  renderDonutChart();
  renderCategoryChart();
  renderAmountChart();
  initFormDefaults();
  initChartObserver();
});

// ─────────────────────────────────────────────────────────────
// Background Particles
// ─────────────────────────────────────────────────────────────
function initParticles() {
  var container = document.getElementById('bgParticles');
  if (!container) return;
  var colors = ['#6366f1', '#06b6d4', '#a855f7', '#22c55e', '#f59e0b'];
  for (var i = 0; i < 18; i++) {
    var p = document.createElement('div');
    p.className = 'particle';
    var size = Math.random() * 300 + 80;
    var color = colors[Math.floor(Math.random() * colors.length)];
    var dur = (Math.random() * 20 + 15) + 's';
    var delay = -(Math.random() * 20) + 's';
    p.style.cssText =
      'width:' + size + 'px; height:' + size + 'px;' +
      'left:' + (Math.random() * 100) + '%;' +
      'top:' + (Math.random() * 100) + '%;' +
      'background: radial-gradient(circle, ' + color + '18 0%, transparent 70%);' +
      '--dur:' + dur + ';' +
      'animation-delay:' + delay + ';' +
      'transform:translate(-50%,-50%);';
    container.appendChild(p);
  }
}

// ─────────────────────────────────────────────────────────────
// Sticky Navbar & Mobile Navigation Drawer
// ─────────────────────────────────────────────────────────────
function initNavbar() {
  var nav = document.getElementById('navbar');
  if (nav) {
    window.addEventListener('scroll', function() {
      nav.classList.toggle('scrolled', window.scrollY > 40);
    });
  }

  var toggleBtn = document.getElementById('navToggle');
  var closeBtn  = document.getElementById('mobileNavClose');
  var backdrop  = document.getElementById('mobileBackdrop');

  if (toggleBtn) {
    toggleBtn.addEventListener('click', openMobileNav);
  }
  if (closeBtn) {
    closeBtn.addEventListener('click', closeMobileNav);
  }
  if (backdrop) {
    backdrop.addEventListener('click', closeMobileNav);
  }
}

function openMobileNav() {
  var mobileNav = document.getElementById('mobileNav');
  var backdrop  = document.getElementById('mobileBackdrop');
  if (mobileNav) mobileNav.classList.add('open');
  if (backdrop) backdrop.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeMobileNav() {
  var mobileNav = document.getElementById('mobileNav');
  var backdrop  = document.getElementById('mobileBackdrop');
  if (mobileNav) mobileNav.classList.remove('open');
  if (backdrop) backdrop.classList.remove('open');
  document.body.style.overflow = '';
}

// ─────────────────────────────────────────────────────────────
// Animated Counters
// ─────────────────────────────────────────────────────────────
function initCounters() {
  var counters = document.querySelectorAll('[data-target]');
  if (!('IntersectionObserver' in window)) {
    counters.forEach(function(c) { animateCounter(c); });
    return;
  }
  var observer = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.5 });
  counters.forEach(function(c) { observer.observe(c); });
}

function animateCounter(el) {
  var target = parseFloat(el.dataset.target);
  var isFloat = !Number.isInteger(target);
  var duration = 2000;
  var start = performance.now();
  function update(now) {
    var progress = Math.min((now - start) / duration, 1);
    var ease = 1 - Math.pow(1 - progress, 3);
    var val = target * ease;
    el.textContent = isFloat
      ? val.toFixed(1)
      : Math.round(val).toLocaleString('en-IN');
    if (progress < 1) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}

// ─────────────────────────────────────────────────────────────
// Range Slider
// ─────────────────────────────────────────────────────────────
function initRangeSlider() {
  var slider = document.getElementById('txn-frequency');
  var val = document.getElementById('txnFreqVal');
  if (!slider || !val) return;
  slider.addEventListener('input', function() { val.textContent = slider.value; });
}

// ─────────────────────────────────────────────────────────────
// Set form defaults
// ─────────────────────────────────────────────────────────────
function initFormDefaults() {
  var now = new Date();
  var timeEl = document.getElementById('txn-time');
  if (timeEl) {
    timeEl.value = String(now.getHours()).padStart(2,'0') + ':' + String(now.getMinutes()).padStart(2,'0');
  }
  var expiry = new Date();
  expiry.setFullYear(expiry.getFullYear() + 3);
  var expiryEl = document.getElementById('expiry-date');
  if (expiryEl) {
    expiryEl.value = expiry.getFullYear() + '-' + String(expiry.getMonth()+1).padStart(2,'0');
  }
}

// ─────────────────────────────────────────────────────────────
// MAIN: Analyze Transaction
// ─────────────────────────────────────────────────────────────
function analyzeTransaction() {
  // Read form values
  var cardType    = document.getElementById('card-type').value;
  var cardStatus  = document.getElementById('card-status').value;
  var cardNumberEl = document.getElementById('card-number');
  var txnAmountEl = document.getElementById('txn-amount');
  var categoryEl  = document.getElementById('merchant-category');
  var txnTimeEl   = document.getElementById('txn-time');
  var locationEl  = document.getElementById('txn-location');
  var freqEl      = document.getElementById('txn-frequency');
  var limitEl     = document.getElementById('credit-limit');
  var expiryEl    = document.getElementById('expiry-date');

  var txnAmount   = parseFloat(txnAmountEl.value);
  var category    = categoryEl.value;
  var txnTime     = txnTimeEl.value;
  var txnLocation = locationEl.value || 'domestic';
  var frequency   = parseInt(freqEl.value) || 3;
  var creditLimit = parseInt(limitEl.value) || 0;
  var expiryDate  = expiryEl.value;

  // Validation
  if (!cardType) {
    showToast('\u26a0\ufe0f', 'Please select a Card Type.', 'warn');
    document.getElementById('card-type').focus();
    return;
  }
  if (!cardStatus) {
    showToast('\u26a0\ufe0f', 'Please select a Card Status.', 'warn');
    document.getElementById('card-status').focus();
    return;
  }
  if (!txnAmount || isNaN(txnAmount) || txnAmount <= 0) {
    showToast('\u26a0\ufe0f', 'Please enter a valid Transaction Amount.', 'warn');
    txnAmountEl.focus();
    return;
  }
  if (!category) {
    showToast('\u26a0\ufe0f', 'Please select a Merchant Category.', 'warn');
    categoryEl.focus();
    return;
  }
  if (!txnTime) {
    showToast('\u26a0\ufe0f', 'Please enter a Transaction Time.', 'warn');
    txnTimeEl.focus();
    return;
  }

  // Show loading state
  showLoading();

  // Run analysis after animation
  runLoadingSteps(function() {
    var payload = {
      cardType: cardType,
      cardStatus: cardStatus,
      txnAmount: txnAmount,
      category: category,
      txnTime: txnTime,
      txnLocation: txnLocation,
      frequency: frequency,
      creditLimit: creditLimit,
      expiryDate: expiryDate
    };

    // Call Python ML Backend (Relative if hosted on unified server, or localhost:5000 if local)
    var apiUrl = (window.location.protocol === 'file:' || window.location.port === '8000')
      ? 'http://localhost:5000/analyze'
      : '/analyze';

    fetch(apiUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    })
    .then(function(response) { return response.json(); })
    .then(function(data) {
      // Calculate local factors for the UI breakdown
      var result = computeFraudScore(payload);
      
      // Override final verdict with ML Model's score
      if (data.score !== undefined) {
        result.score = data.score;
        var verdictData = getVerdict(data.score);
        result.verdict = verdictData.verdict;
        result.verdictClass = verdictData.verdictClass;
        result.recommendations = verdictData.recommendations;
        
        // Show actual ML probability
        if (data.ml_probability !== undefined) {
          result.probability = (data.ml_probability * 100).toFixed(2) + '% fraud probability (ML)';
        }
      }
      
      showResult(result, payload);
    })
    .catch(function(error) {
      console.error('Backend Error:', error);
      showToast('\u26a0\ufe0f', 'ML Backend unreachable. Using local logic.', 'warn');
      var result = computeFraudScore(payload);
      showResult(result, payload);
    });
  });
}

// ─────────────────────────────────────────────────────────────
// Fraud Scoring Engine
// ─────────────────────────────────────────────────────────────
function computeFraudScore(params) {
  var cardType    = params.cardType;
  var cardStatus  = params.cardStatus;
  var txnAmount   = params.txnAmount;
  var category    = params.category;
  var txnTime     = params.txnTime;
  var txnLocation = params.txnLocation;
  var frequency   = params.frequency;
  var creditLimit = params.creditLimit;
  var expiryDate  = params.expiryDate;

  var factors = [];
  var totalScore = 0;

  // 1. Card Status Factor
  var statusScore = 0, statusColor = '#22c55e', statusNote = '';
  if (cardStatus === 'blocked') {
    statusScore = 100; statusColor = '#ef4444';
    statusNote = 'Transaction on a blocked card – extremely high risk';
  } else if (cardStatus === 'expired') {
    var now = new Date();
    var expiry = expiryDate ? new Date(expiryDate + '-01') : new Date(2020, 0, 1);
    statusScore = expiry < now ? 90 : 15;
    statusColor = expiry < now ? '#ef4444' : '#22c55e';
    statusNote = expiry < now ? 'Card is expired – suspicious activity' : 'Card in valid period';
  } else {
    statusScore = 5; statusColor = '#22c55e';
    statusNote = 'Active card – no status risk';
  }
  factors.push({ name: 'Card Status', score: statusScore, weight: WEIGHTS.cardStatus, color: statusColor, note: statusNote });
  totalScore += (statusScore / 100) * WEIGHTS.cardStatus;

  // 2. Amount Factor
  var avgAmount = FRAUD_STATS.avgLegitAmount;
  var amountScore = 0, amountColor = '#22c55e', amountNote = '';
  if (txnAmount < 100) {
    amountScore = 35; amountColor = '#f59e0b';
    amountNote = 'Very small amount – possible card-testing';
  } else if (txnAmount < 500) {
    amountScore = 20; amountColor = '#22c55e';
    amountNote = 'Low-value transaction – minimal risk';
  } else if (txnAmount <= avgAmount * 1.5) {
    amountScore = 10; amountColor = '#22c55e';
    amountNote = 'Within normal spending range';
  } else if (txnAmount <= avgAmount * 3) {
    amountScore = 40; amountColor = '#f59e0b';
    amountNote = 'Above-average transaction amount';
  } else if (txnAmount <= avgAmount * 5) {
    amountScore = 65; amountColor = '#f97316';
    amountNote = 'Significantly high transaction amount';
  } else {
    amountScore = 85; amountColor = '#ef4444';
    amountNote = 'Extremely large transaction – high suspicion';
  }
  factors.push({ name: 'Transaction Amount', score: amountScore, weight: WEIGHTS.amount, color: amountColor, note: amountNote });
  totalScore += (amountScore / 100) * WEIGHTS.amount;

  // 3. Time Factor
  var timeParts = txnTime.split(':');
  var hours = parseInt(timeParts[0]) || 0;
  var minutes = parseInt(timeParts[1]) || 0;
  var timeHour = hours + minutes / 60;
  var timeScore = 0, timeColor = '#22c55e', timeNote = '';
  if (timeHour >= 0 && timeHour < 4) {
    timeScore = 75; timeColor = '#ef4444';
    timeNote = 'Midnight/early-morning – high-risk window (0\u20134 AM)';
  } else if (timeHour >= 4 && timeHour < 7) {
    timeScore = 45; timeColor = '#f59e0b';
    timeNote = 'Pre-business hours – elevated risk (4\u20137 AM)';
  } else if (timeHour >= 7 && timeHour < 22) {
    timeScore = 8; timeColor = '#22c55e';
    timeNote = 'Normal business hours – low temporal risk';
  } else {
    timeScore = 30; timeColor = '#f59e0b';
    timeNote = 'Late evening – slightly elevated risk (10 PM+)';
  }
  factors.push({ name: 'Transaction Time', score: timeScore, weight: WEIGHTS.time, color: timeColor, note: timeNote });
  totalScore += (timeScore / 100) * WEIGHTS.time;

  // 4. Location Factor
  var locScore = txnLocation === 'international' ? 65 : 5;
  var locColor = txnLocation === 'international' ? '#f97316' : '#22c55e';
  var locNote = txnLocation === 'international'
    ? 'International transaction – 3\xd7 higher fraud probability'
    : 'Domestic transaction – standard risk profile';
  factors.push({ name: 'Geographic Location', score: locScore, weight: WEIGHTS.location, color: locColor, note: locNote });
  totalScore += (locScore / 100) * WEIGHTS.location;

  // 5. Category Factor
  var catRate = FRAUD_STATS.categoryFraudRate[category] || 0.5;
  var catScore = Math.round(((catRate - 0.45) / (0.55 - 0.45)) * 100);
  catScore = Math.max(0, Math.min(100, catScore));
  var catColor = catScore < 40 ? '#22c55e' : catScore < 65 ? '#f59e0b' : '#ef4444';
  var highRiskCats = ['ATM Withdrawal', 'Fund Transfer', 'Healthcare', 'Salary Credit'];
  var catNote = highRiskCats.indexOf(category) >= 0
    ? category + ' – above-average fraud category'
    : category + ' – standard-risk merchant category';
  factors.push({ name: 'Merchant Category', score: catScore, weight: WEIGHTS.category, color: catColor, note: catNote });
  totalScore += (catScore / 100) * WEIGHTS.category;

  // 6. Frequency Factor
  var freqScore = 0, freqColor = '#22c55e', freqNote = '';
  if (frequency <= 3) {
    freqScore = 5;  freqColor = '#22c55e'; freqNote = 'Normal transaction frequency';
  } else if (frequency <= 6) {
    freqScore = 20; freqColor = '#22c55e'; freqNote = 'Slightly elevated – within normal range';
  } else if (frequency <= 10) {
    freqScore = 50; freqColor = '#f59e0b'; freqNote = 'High frequency – possible card-testing pattern';
  } else {
    freqScore = 85; freqColor = '#ef4444'; freqNote = 'Excessive frequency – strong card-testing signal';
  }
  factors.push({ name: 'Transaction Frequency', score: freqScore, weight: WEIGHTS.frequency, color: freqColor, note: freqNote });
  totalScore += (freqScore / 100) * WEIGHTS.frequency;

  // 7. Credit Utilization Factor
  var utilScore = 5, utilColor = '#22c55e', utilNote = 'N/A for debit cards';
  if (creditLimit > 0) {
    var util = txnAmount / creditLimit;
    if (util > 1) {
      utilScore = 90; utilColor = '#ef4444';
      utilNote = 'Transaction (\u20b9' + txnAmount.toLocaleString('en-IN') + ') exceeds credit limit!';
    } else if (util > 0.8) {
      utilScore = 60; utilColor = '#f97316';
      utilNote = Math.round(util * 100) + '% credit utilization – very high';
    } else if (util > 0.5) {
      utilScore = 30; utilColor = '#f59e0b';
      utilNote = Math.round(util * 100) + '% credit utilization – moderate';
    } else {
      utilScore = 5; utilColor = '#22c55e';
      utilNote = Math.round(util * 100) + '% credit utilization – normal';
    }
  }
  factors.push({ name: 'Credit Utilization', score: utilScore, weight: WEIGHTS.creditUtil, color: utilColor, note: utilNote });
  totalScore += (utilScore / 100) * WEIGHTS.creditUtil;

  // Final Score
  var finalScore = Math.round(Math.min(100, totalScore));
  var verdictData = getVerdict(finalScore);

  return {
    score: finalScore,
    verdict: verdictData.verdict,
    verdictClass: verdictData.verdictClass,
    probability: verdictData.probability,
    recommendations: verdictData.recommendations,
    factors: factors
  };
}

function getVerdict(score) {
  if (score < 15) {
    return {
      verdict: 'Very Low Risk', verdictClass: 'safe',
      probability: (score * 0.1).toFixed(2) + '% fraud probability',
      recommendations: [
        { type: 'safe', icon: '\u2705', text: 'Transaction appears legitimate. Approve normally.' },
        { type: 'safe', icon: '\uD83D\uDD12', text: 'Standard fraud monitoring is sufficient for this transaction.' }
      ]
    };
  }
  if (score < 35) {
    return {
      verdict: 'Low Risk', verdictClass: 'low',
      probability: (score * 0.15).toFixed(2) + '% fraud probability',
      recommendations: [
        { type: 'safe', icon: '\u2705', text: 'Transaction looks safe. Standard approval recommended.' },
        { type: 'warn', icon: '\uD83D\uDC40', text: 'Continue monitoring this card for pattern changes.' }
      ]
    };
  }
  if (score < 55) {
    return {
      verdict: 'Medium Risk', verdictClass: 'medium',
      probability: (score * 0.2).toFixed(2) + '% fraud probability',
      recommendations: [
        { type: 'warn', icon: '\u26a0\ufe0f', text: 'Elevated risk detected. Consider secondary authentication.' },
        { type: 'warn', icon: '\uD83D\uDCF1', text: 'Send OTP verification to cardholder before proceeding.' },
        { type: 'safe', icon: '\uD83D\uDCCA', text: 'Review recent transaction history before approval.' }
      ]
    };
  }
  if (score < 75) {
    return {
      verdict: 'High Risk', verdictClass: 'high',
      probability: (score * 0.25).toFixed(2) + '% fraud probability',
      recommendations: [
        { type: 'danger', icon: '\uD83D\uDEA8', text: 'High fraud risk. Require additional verification immediately.' },
        { type: 'warn', icon: '\uD83D\uDCDE', text: 'Contact cardholder directly to confirm this transaction.' },
        { type: 'danger', icon: '\uD83D\uDD10', text: 'Temporarily hold transaction pending cardholder confirmation.' }
      ]
    };
  }
  return {
    verdict: 'Likely Fraud', verdictClass: 'fraud',
    probability: Math.min(99, score * 0.9).toFixed(1) + '% fraud probability',
    recommendations: [
      { type: 'danger', icon: '\uD83D\uDED1', text: 'BLOCK THIS TRANSACTION. High probability of fraud detected.' },
      { type: 'danger', icon: '\uD83D\uDD12', text: 'Temporarily freeze the card until cardholder is verified.' },
      { type: 'danger', icon: '\uD83D\uDCCB', text: 'File a fraud incident report and notify the cardholder immediately.' },
      { type: 'warn', icon: '\uD83D\uDD0D', text: 'Investigate recent transactions on this account for additional fraud.' }
    ]
  };
}

// ─────────────────────────────────────────────────────────────
// Loading Animation
// ─────────────────────────────────────────────────────────────
function showLoading() {
  var idle    = document.getElementById('resultIdle');
  var loading = document.getElementById('resultLoading');
  var output  = document.getElementById('resultOutput');
  var btn     = document.getElementById('analyzeBtn');

  if (idle)    idle.style.display    = 'none';
  if (output)  output.style.display  = 'none';
  if (loading) loading.style.display = 'flex';
  if (btn)     btn.disabled = true;

  var steps = [
    'Validating card details...',
    'Analyzing transaction amount...',
    'Checking temporal patterns...',
    'Evaluating merchant category...',
    'Computing risk vectors...',
    'Generating fraud score...'
  ];
  var container = document.getElementById('loadingSteps');
  if (container) {
    container.innerHTML = steps.map(function(s, i) {
      return '<div class="loading-step" id="lstep_' + i + '">' +
             '<div class="loading-step-dot"></div>' +
             '<span>' + s + '</span>' +
             '</div>';
    }).join('');
  }
}

function runLoadingSteps(callback) {
  var steps = document.querySelectorAll('.loading-step');
  var idx = 0;

  function nextStep() {
    if (idx >= steps.length) {
      setTimeout(callback, 200);
      return;
    }
    var step = steps[idx];
    step.classList.add('active');
    setTimeout(function() {
      step.classList.remove('active');
      step.classList.add('done');
      var dot = step.querySelector('.loading-step-dot');
      if (dot) dot.textContent = '';
      idx++;
      setTimeout(nextStep, 80);
    }, 280);
  }

  nextStep();
}

// ─────────────────────────────────────────────────────────────
// Display Result
// ─────────────────────────────────────────────────────────────
function showResult(result, params) {
  var loading = document.getElementById('resultLoading');
  var output  = document.getElementById('resultOutput');
  var btn     = document.getElementById('analyzeBtn');

  if (loading) loading.style.display = 'none';
  if (output)  output.style.display  = 'flex';
  if (btn)     btn.disabled = false;

  // Verdict
  var verdictEl = document.getElementById('riskVerdict');
  if (verdictEl) {
    verdictEl.textContent = result.verdict;
    verdictEl.className   = 'risk-verdict verdict-' + result.verdictClass;
  }

  var probEl = document.getElementById('riskProbability');
  if (probEl) probEl.textContent = 'Fraud Probability: ' + result.probability;

  // Badge icon
  var icon = document.getElementById('riskIcon');
  if (icon) {
    icon.className = 'risk-badge-icon badge-' + result.verdictClass;
    var svgPath = result.verdictClass === 'fraud'
      ? '<path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/>'
      : (result.verdictClass === 'high' || result.verdictClass === 'medium')
      ? '<circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>'
      : '<path d="M12 2L3 7v5c0 5.25 3.75 10.15 9 11.35C17.25 22.15 21 17.25 21 12V7L12 2z"/><path d="M9 12l2 2 4-4" stroke-linecap="round" stroke-linejoin="round"/>';
    var svg = icon.querySelector('svg');
    if (svg) svg.innerHTML = svgPath;
  }

  // Score card border color
  var scoreCard = document.getElementById('riskScoreCard');
  if (scoreCard) {
    scoreCard.style.borderColor = result.verdictClass === 'fraud'   ? 'rgba(239,68,68,0.4)'
      : result.verdictClass === 'high'   ? 'rgba(249,115,22,0.4)'
      : result.verdictClass === 'medium' ? 'rgba(245,158,11,0.4)'
      : 'rgba(34,197,94,0.3)';
  }

  // Animate gauge
  animateGauge(result.score);

  // Render factors and recommendations
  renderFactors(result.factors);
  renderRecommendations(result.recommendations);

  // Add to history
  addToHistory(result, params);

  // Scroll into view
  if (output) {
    setTimeout(function() {
      output.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }, 100);
  }
}

function animateGauge(score) {
  var totalArc = 283;
  var gaugeFill   = document.getElementById('gaugeFill');
  var gaugeNeedle = document.getElementById('gaugeNeedle');
  var gaugeNumber = document.getElementById('gaugeNumber');
  if (!gaugeFill || !gaugeNeedle || !gaugeNumber) return;

  var current = 0;
  var duration = 1200;
  var start = performance.now();

  function update(now) {
    var progress = Math.min((now - start) / duration, 1);
    var ease = 1 - Math.pow(1 - progress, 3);
    current = score * ease;

    gaugeNumber.textContent = Math.round(current);

    var offset = totalArc - (totalArc * current / 100);
    gaugeFill.style.strokeDashoffset = offset;

    // Move needle along the semicircle arc
    var angle = Math.PI * (current / 100);
    var cx = 110 + Math.cos(Math.PI - angle) * 90;
    var cy = 110 - Math.sin(angle) * 90;
    gaugeNeedle.setAttribute('cx', cx.toFixed(1));
    gaugeNeedle.setAttribute('cy', cy.toFixed(1));

    if (progress < 1) requestAnimationFrame(update);
  }
  requestAnimationFrame(update);
}

function renderFactors(factors) {
  var container = document.getElementById('factorsList');
  if (!container) return;
  container.innerHTML = factors.map(function(f) {
    return '<div class="factor-item">' +
      '<div class="factor-row">' +
        '<div class="factor-name">' +
          '<div class="factor-dot" style="background:' + f.color + '"></div>' +
          f.name +
        '</div>' +
        '<span class="factor-score" style="color:' + f.color + '">' + f.score + '/100</span>' +
      '</div>' +
      '<div class="factor-bar-bg">' +
        '<div class="factor-bar" style="background:' + f.color + ';width:0%" data-width="' + f.score + '"></div>' +
      '</div>' +
      '<div style="font-size:0.72rem;color:var(--text-muted);margin-top:2px;">' + f.note + '</div>' +
    '</div>';
  }).join('');

  // Animate bars after paint
  setTimeout(function() {
    container.querySelectorAll('.factor-bar').forEach(function(bar) {
      bar.style.width = bar.dataset.width + '%';
    });
  }, 150);
}

function renderRecommendations(recommendations) {
  var container = document.getElementById('recommendationsList');
  if (!container) return;
  var typeMap = { safe: 'rec-safe', warn: 'rec-warn', danger: 'rec-danger' };
  container.innerHTML = recommendations.map(function(r) {
    return '<div class="rec-item ' + (typeMap[r.type] || 'rec-safe') + '">' +
      '<span class="rec-icon">' + r.icon + '</span>' +
      '<span>' + r.text + '</span>' +
    '</div>';
  }).join('');
}

// ─────────────────────────────────────────────────────────────
// Mark Transaction
// ─────────────────────────────────────────────────────────────
function markTransaction(type) {
  if (type === 'safe') {
    showToast('\u2705', 'Transaction marked as safe and approved.', 'safe');
  } else {
    showToast('\uD83D\uDEA8', 'Fraud report filed. Card flagged for review.', 'danger');
  }
  if (analysisHistory.length > 0) {
    analysisHistory[0].userVerdict = type;
    renderHistory();
  }
}

// ─────────────────────────────────────────────────────────────
// Reset Form
// ─────────────────────────────────────────────────────────────
function resetForm() {
  var fields = ['card-type', 'card-status', 'card-number', 'txn-amount', 'merchant-category'];
  fields.forEach(function(id) {
    var el = document.getElementById(id);
    if (el) el.value = '';
  });

  var locEl = document.getElementById('txn-location');
  if (locEl) locEl.value = 'domestic';

  var freqEl = document.getElementById('txn-frequency');
  var freqVal = document.getElementById('txnFreqVal');
  if (freqEl) freqEl.value = 3;
  if (freqVal) freqVal.textContent = 3;

  var limitEl = document.getElementById('credit-limit');
  if (limitEl) limitEl.value = '0';

  initFormDefaults();

  var output = document.getElementById('resultOutput');
  var idle   = document.getElementById('resultIdle');
  if (output) output.style.display = 'none';
  if (idle)   idle.style.display   = 'flex';

  window.scrollTo({ top: document.getElementById('detector').offsetTop - 80, behavior: 'smooth' });
}

// ─────────────────────────────────────────────────────────────
// History
// ─────────────────────────────────────────────────────────────
function addToHistory(result, params) {
  analysisCount++;
  var now = new Date();
  var h = now.getHours();
  var m = now.getMinutes();
  var ampm = h >= 12 ? 'PM' : 'AM';
  h = h % 12;
  h = h ? h : 12;
  var timeStr = h + ':' + String(m).padStart(2, '0') + ' ' + ampm;
  var entry = {
    id: analysisCount,
    time: timeStr,
    cardType: params.cardType || '\u2014',
    category: params.category || '\u2014',
    amount: params.txnAmount,
    score: result.score,
    verdictClass: result.verdictClass,
    verdict: result.verdict,
    userVerdict: null
  };
  analysisHistory.unshift(entry);
  renderHistory();
}

function renderHistory() {
  var empty = document.getElementById('historyEmpty');
  var table = document.getElementById('historyTable');
  var tbody = document.getElementById('historyBody');
  if (!empty || !table || !tbody) return;

  if (analysisHistory.length === 0) {
    empty.style.display = 'flex';
    table.style.display = 'none';
    return;
  }
  empty.style.display = 'none';
  table.style.display = 'block';

  var verdictMap = {
    safe: '#22c55e', low: '#84cc16', medium: '#f59e0b', high: '#f97316', fraud: '#ef4444'
  };

  tbody.innerHTML = analysisHistory.map(function(h) {
    var color = verdictMap[h.verdictClass] || '#94a3b8';
    var cardTypeLabel = {
      'debit': 'Debit',
      'credit-classic': 'CC Classic',
      'credit-gold': 'CC Gold',
      'credit-platinum': 'CC Platinum'
    }[h.cardType] || h.cardType;

    var uvBadge = h.userVerdict
      ? '<span style="font-size:0.75rem;color:' + (h.userVerdict === 'safe' ? '#22c55e' : '#ef4444') + '">' +
          (h.userVerdict === 'safe' ? '\u2705 Safe' : '\uD83D\uDEA8 Fraud') +
        '</span>'
      : '';

    return '<tr>' +
      '<td style="color:var(--text-secondary);font-family:var(--font-mono)">' + h.time + '</td>' +
      '<td>' + cardTypeLabel + '</td>' +
      '<td>' + h.category + '</td>' +
      '<td style="font-family:var(--font-mono)">\u20b9' + h.amount.toLocaleString('en-IN') + '</td>' +
      '<td><span class="score-badge" style="background:' + color + '22;color:' + color + ';border:1px solid ' + color + '44">' + h.score + '</span></td>' +
      '<td><span class="verdict-chip chip-' + h.verdictClass + '">' + h.verdict + '</span> ' + uvBadge + '</td>' +
      '<td><button class="del-btn" onclick="removeHistory(' + h.id + ')">Remove</button></td>' +
    '</tr>';
  }).join('');
}

function removeHistory(id) {
  analysisHistory = analysisHistory.filter(function(h) { return h.id !== id; });
  renderHistory();
}

// ─────────────────────────────────────────────────────────────
// Analytics Charts (Architectural Editorial Styling)
// ─────────────────────────────────────────────────────────────
function renderCategoryChart() {
  var data = FRAUD_STATS.categoryFraudRate;
  var container = document.getElementById('categoryChart');
  if (!container) return;

  var values = Object.values(data);
  var max = Math.max.apply(null, values);

  var colors = [
    '#0e0e0e', '#1c1c1c', '#282828', '#343434', '#404040',
    '#4d4d4d', '#595959', '#666666', '#737373', '#808080',
    '#171717', '#2b2b2b', '#3b3b3b', '#0e0e0e'
  ];

  container.innerHTML = Object.keys(data).map(function(cat, i) {
    var rate = data[cat];
    var heightPx = Math.round((rate / max) * 160);
    var color = colors[i % colors.length];
    var label = cat.length > 10 ? cat.substring(0, 9) + '\u2026' : cat;
    return '<div class="chart-bar-group" title="' + cat + ': ' + rate.toFixed(3) + '% fraud rate">' +
      '<div class="chart-bar-val">' + rate.toFixed(2) + '%</div>' +
      '<div class="chart-bar-wrap">' +
        '<div class="chart-bar" style="background:' + color + ';height:0" data-height="' + heightPx + 'px"></div>' +
      '</div>' +
      '<div class="chart-bar-label">' + label + '</div>' +
    '</div>';
  }).join('');

  // Animate bars
  setTimeout(function() {
    container.querySelectorAll('.chart-bar').forEach(function(bar) {
      bar.style.transition = 'height 1s cubic-bezier(0.16,1,0.3,1)';
      bar.style.height = bar.dataset.height;
    });
  }, 400);
}

function renderDonutChart() {
  var data = FRAUD_STATS.cardDistribution;
  var total = Object.values(data).reduce(function(a, b) { return a + b; }, 0);
  var colors = ['#0e0e0e', '#383838', '#686868', '#9e9e9e'];
  var svg = document.getElementById('donutChart');
  var legend = document.getElementById('donutLegend');
  if (!svg || !legend) return;

  var cx = 100, cy = 100, r = 70, strokeWidth = 22;
  var circumference = 2 * Math.PI * r;
  var offset = 0;
  var paths = '';
  var entries = Object.keys(data);

  entries.forEach(function(type, i) {
    var count = data[type];
    var fraction = count / total;
    var dashLen = fraction * circumference;
    var color = colors[i];
    paths += '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '"' +
      ' fill="none" stroke="' + color + '" stroke-width="' + strokeWidth + '"' +
      ' stroke-dasharray="' + dashLen + ' ' + circumference + '"' +
      ' stroke-dashoffset="' + (-offset) + '"' +
      ' stroke-linecap="butt"' +
      ' transform="rotate(-90 ' + cx + ' ' + cy + ')"' +
      ' style="cursor:pointer;transition:opacity 0.2s"' +
      ' onmouseover="this.style.opacity=\'0.75\'"' +
      ' onmouseout="this.style.opacity=\'1\'"' +
      '/>';
    offset += dashLen;
  });

  svg.innerHTML =
    '<circle cx="' + cx + '" cy="' + cy + '" r="' + r + '" fill="none" stroke="rgba(14,14,14,0.08)" stroke-width="' + strokeWidth + '"/>' +
    paths +
    '<text x="' + cx + '" y="' + (cy-6) + '" text-anchor="middle" fill="#0e0e0e" font-size="20" font-weight="700" font-family="Plus Jakarta Sans, sans-serif">' + (total/1000).toFixed(0) + 'K</text>' +
    '<text x="' + cx + '" y="' + (cy+14) + '" text-anchor="middle" fill="#7e7e79" font-size="8.5" font-weight="700" letter-spacing="1px" font-family="Plus Jakarta Sans, sans-serif">PORTFOLIO</text>';

  legend.innerHTML = entries.map(function(type, i) {
    return '<div class="legend-item">' +
      '<div class="legend-dot" style="background:' + colors[i] + '"></div>' +
      '<span class="legend-label">' + type + '</span>' +
      '<span class="legend-value">' + data[type].toLocaleString('en-IN') + '</span>' +
    '</div>';
  }).join('');
}

function renderAmountChart() {
  var data = FRAUD_STATS.amountFraudRate;
  var container = document.getElementById('amountChart');
  if (!container) return;
  var values = Object.values(data);
  var max = Math.max.apply(null, values);
  var colors = ['#15803d', '#b45309', '#c2410c', '#b91c1c'];

  container.innerHTML = Object.keys(data).map(function(range, i) {
    var rate = data[range];
    var pct = ((rate / max) * 100).toFixed(0);
    var color = colors[i];
    return '<div class="bar-row">' +
      '<span class="bar-label">' + range + '</span>' +
      '<div class="bar-track">' +
        '<div class="bar-fill" style="background:' + color + ';width:0%" data-width="' + pct + '%"></div>' +
      '</div>' +
      '<span class="bar-pct" style="color:' + color + '">' + rate.toFixed(2) + '%</span>' +
    '</div>';
  }).join('');

  setTimeout(function() {
    container.querySelectorAll('.bar-fill').forEach(function(bar) {
      bar.style.transition = 'width 1s cubic-bezier(0.16,1,0.3,1)';
      bar.style.width = bar.dataset.width;
    });
  }, 600);
}

// ─────────────────────────────────────────────────────────────
// Chart Intersection Observer (for scroll-triggered animations)
// ─────────────────────────────────────────────────────────────
function initChartObserver() {
  if (!('IntersectionObserver' in window)) return;
  var ioCharts = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting) {
        entry.target.querySelectorAll('[data-width]').forEach(function(el) {
          setTimeout(function() { el.style.width = el.dataset.width; }, 200);
        });
        entry.target.querySelectorAll('[data-height]').forEach(function(el) {
          setTimeout(function() { el.style.height = el.dataset.height; }, 200);
        });
      }
    });
  }, { threshold: 0.3 });

  document.querySelectorAll('.chart-card, .analytics-grid').forEach(function(el) {
    ioCharts.observe(el);
  });
}

// ─────────────────────────────────────────────────────────────
// Preset Profile Loader (Debit / Gold / Platinum High Risk)
// ─────────────────────────────────────────────────────────────
function loadPreset(type) {
  var cardTypeEl    = document.getElementById('card-type');
  var cardStatusEl  = document.getElementById('card-status');
  var cardNumberEl  = document.getElementById('card-number');
  var txnAmountEl   = document.getElementById('txn-amount');
  var categoryEl    = document.getElementById('merchant-category');
  var txnTimeEl     = document.getElementById('txn-time');
  var locationEl    = document.getElementById('txn-location');
  var freqEl        = document.getElementById('txn-frequency');
  var freqValEl     = document.getElementById('txnFreqVal');
  var limitEl       = document.getElementById('credit-limit');
  var expiryEl      = document.getElementById('expiry-date');

  if (type === 'debit') {
    if (cardTypeEl)   cardTypeEl.value   = 'debit';
    if (cardStatusEl) cardStatusEl.value = 'active';
    if (cardNumberEl) cardNumberEl.value = '4821';
    if (txnAmountEl)  txnAmountEl.value  = '1250';
    if (categoryEl)   categoryEl.value   = 'Groceries';
    if (txnTimeEl)    txnTimeEl.value    = '14:30';
    if (locationEl)   locationEl.value   = 'domestic';
    if (freqEl)       freqEl.value       = '2';
    if (freqValEl)    freqValEl.textContent = '2';
    if (limitEl)      limitEl.value      = '0';
    if (expiryEl)     expiryEl.value     = '2027-08';
    showToast('✓', 'Standard Debit profile loaded', 'safe');
  } else if (type === 'gold') {
    if (cardTypeEl)   cardTypeEl.value   = 'credit-gold';
    if (cardStatusEl) cardStatusEl.value = 'active';
    if (cardNumberEl) cardNumberEl.value = '9012';
    if (txnAmountEl)  txnAmountEl.value  = '28500';
    if (categoryEl)   categoryEl.value   = 'Dining';
    if (txnTimeEl)    txnTimeEl.value    = '20:45';
    if (locationEl)   locationEl.value   = 'domestic';
    if (freqEl)       freqEl.value       = '4';
    if (freqValEl)    freqValEl.textContent = '4';
    if (limitEl)      limitEl.value      = '200000';
    if (expiryEl)     expiryEl.value     = '2028-11';
    showToast('✓', 'Gold Credit profile loaded', 'warn');
  } else if (type === 'highrisk') {
    if (cardTypeEl)   cardTypeEl.value   = 'credit-platinum';
    if (cardStatusEl) cardStatusEl.value = 'active';
    if (cardNumberEl) cardNumberEl.value = '7731';
    if (txnAmountEl)  txnAmountEl.value  = '480000';
    if (categoryEl)   categoryEl.value   = 'Fund Transfer';
    if (txnTimeEl)    txnTimeEl.value    = '03:15';
    if (locationEl)   locationEl.value   = 'international';
    if (freqEl)       freqEl.value       = '14';
    if (freqValEl)    freqValEl.textContent = '14';
    if (limitEl)      limitEl.value      = '500000';
    if (expiryEl)     expiryEl.value     = '2026-05';
    showToast('⚠', 'Platinum High-Risk profile loaded', 'danger');
  }

  var detector = document.getElementById('detector');
  if (detector) {
    detector.scrollIntoView({ behavior: 'smooth' });
  }
}

// ─────────────────────────────────────────────────────────────
// Toast Notifications
// ─────────────────────────────────────────────────────────────
function showToast(icon, message, type) {
  var toast     = document.getElementById('toast');
  var toastIcon = document.getElementById('toastIcon');
  var toastMsg  = document.getElementById('toastMsg');
  if (!toast || !toastIcon || !toastMsg) return;

  var borderColors = { safe: '#15803d', warn: '#b45309', danger: '#b91c1c' };
  var col = borderColors[type] || 'rgba(255,255,255,0.2)';

  toastIcon.textContent   = icon;
  toastMsg.textContent    = message;
  toast.style.borderColor = col;

  toast.classList.remove('show');
  void toast.offsetWidth;
  toast.classList.add('show');
  setTimeout(function() { toast.classList.remove('show'); }, 3500);
}
