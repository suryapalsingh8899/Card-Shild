# -*- coding: utf-8 -*-
"""
Exhaustive Chapters 1 to 3 generation for CardShield Academic Project Report
Provides deep academic prose, mathematical formulations, and engineering diagrams.
"""

import os
from docx.shared import Inches, Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from generate_all import set_cell_background, set_cell_margins, set_table_borders

def add_p(doc, text, indent=True, space_after=6):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.5)
    run = p.add_run(text)
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def add_chapter_title(doc, chap_num_str, title_str):
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.line_spacing = 1.5
    p1.paragraph_format.space_before = Pt(12)
    p1.paragraph_format.space_after = Pt(2)
    run1 = p1.add_run(chap_num_str.upper())
    run1.bold = True
    run1.font.name = 'Times New Roman'
    run1.font.size = Pt(14)
    
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.line_spacing = 1.5
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(16)
    run2 = p2.add_run(title_str.upper())
    run2.bold = True
    run2.font.name = 'Times New Roman'
    run2.font.size = Pt(14)

def add_sec_heading(doc, sec_str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(sec_str)
    run.bold = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def add_subsec_heading(doc, subsec_str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run(subsec_str)
    run.bold = True
    run.italic = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def add_fig(doc, img_path, caption_str, width_in=5.4):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(10)
        p_img.paragraph_format.space_after = Pt(4)
        p_img.paragraph_format.first_line_indent = Inches(0)
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_in))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(12)
        p_cap.paragraph_format.first_line_indent = Inches(0)
        run_cap = p_cap.add_run(caption_str)
        run_cap.bold = True
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(11)

def add_chapters_1_to_3(doc):
    # =========================================================
    # CHAPTER 1: INTRODUCTION
    # =========================================================
    add_chapter_title(doc, "Chapter 1", "Introduction")

    add_sec_heading(doc, "1.1 Motivation & Historical Evolution of ATM Banking Fraud")
    add_p(doc, "Over the past four decades, the global financial services landscape has undergone an extraordinary technological revolution. The mechanization and subsequent digitization of financial transactions shifted retail banking from physical brick-and-mortar branches into a ubiquitous, round-the-clock Automated Teller Machine (ATM) and point-of-sale (POS) terminal infrastructure. Modern consumers depend heavily on magnetic stripe, EMV chip, and contactless payment cards for essential cash withdrawals, daily subsistence procurement, business commerce, and international financial settlement. According to reports published by international financial watchdogs and payment card consortiums (such as VISA, Mastercard, RuPay, and American Express), billions of electronic card transactions are authorized daily across more than 3.5 million networked ATM terminals worldwide.")
    add_p(doc, "However, this immense transactional velocity and the convenience of distributed banking access have simultaneously transformed payment card infrastructures into the primary target of sophisticated global cybercrime cartels. Financial fraud has evolved from rudimentary, opportunistic purse-snatching into highly organized, automated cyber threats executed by transnational criminal syndicates.")
    add_p(doc, "In the early eras of ATM deployment, attacks were primarily physical, involving brute-force safecracking or the physical extraction of the cash dispenser using heavy machinery. As physical security reinforced ATM chassis, adversaries pivoted toward electronic and software exploitation. Criminals began deploying ultra-thin physical skimming modules within ATM card insertion bezels to capture unencrypted magnetic stripe Track-2 data. Concurrently, miniature pinhole cameras and false tactile keypad overlays recorded cardholder Personal Identification Numbers (PINs).")
    add_p(doc, "In recent years, the threat landscape has intensified with the advent of deep-insert skimmers—microscopic devices placed directly inside the motorized card reader mechanism, rendering them completely invisible to external visual inspection. Furthermore, malicious syndicates have adapted to EMV chip cards by deploying 'shimming' devices—paper-thin microchip bypass shims that intercept communications between the chip and the terminal. These physical-electronic exploits are paired with automated dark-web marketplaces and botnets that execute synchronized cash-out attacks across disparate geographic coordinates within minutes.")
    add_p(doc, "When such attacks occur, traditional banking defense architectures—which rely on end-of-day batch ledger reconciliations or manual human review queues—fail catastrophically. Millions of dollars can be siphoned across dispersed geographic ATM terminals before a compliance auditor even receives an alert ticket. Furthermore, the operational and reputational damage inflicted on banking institutions is severe: compromised consumer trust, regulatory fines from financial watchdogs, and immense customer service overhead. Consequently, there is an imperative academic and industrial necessity to formulate autonomous, real-time cyber defense mechanisms that inspect transaction metadata, evaluate multi-dimensional behavioral context, and execute defensive lockdowns within sub-second latencies.")

    add_sec_heading(doc, "1.2 ATM Architecture & Vulnerability Landscape")
    add_p(doc, "An Automated Teller Machine is a specialized cyber-physical computing system comprising an internal industrial PC (typically running an embedded operating system such as Windows IoT or Linux), hardware peripherals (card reader, encrypting PIN pad, cash dispenser, receipt printer, and journal printer), and network communication controllers operating over CEN/XFS (Extensions for Financial Services) APIs. The terminal communicates with the banking institution's host authorization switch using standardized financial messaging protocols, predominantly ISO 8583.")
    add_p(doc, "Despite stringent security certifications, vulnerabilities exist across multiple touchpoints in the ATM transaction lifecycle:")
    add_p(doc, "• Physical Ingress Vulnerabilities: Card reader bezels remain accessible to the public, allowing malicious actors to attach skimming bezels or insert reader shims without immediate physical detection.")
    add_p(doc, "• Peripheral Bus Exploitation: Legacy ATM architectures connect the central PC core to internal peripherals via unauthenticated USB or serial communication buses, enabling 'Black Box' attacks where attackers drill into the chassis to connect external hardware directly to the cash dispenser.")
    add_p(doc, "• Network Wiretapping: Remote ATMs deployed at off-site retail locations often communicate over cellular or unshielded DSL uplinks, exposing unencrypted message fragments to packet sniffing and man-in-the-middle replay attacks.")
    add_p(doc, "• Behavioral Blind Spots: ATM host switches historically evaluate whether the entered PIN matches the cryptographically signed PIN block stored in the Hardware Security Module (HSM). However, the host switch remains blind to whether the physical behavior preceding the transaction (e.g., rapid consecutive attempts, abnormal withdrawal amounts, or impossible travel times) aligns with legitimate cardholder patterns.")

    add_sec_heading(doc, "1.3 Threat Vector Taxonomy")
    add_p(doc, "To establish a rigorous defense framework, CardShield categorizes contemporary ATM card attack vectors into distinct operational classes:")
    add_p(doc, "1. Physical Skimming & Cloning: Extraction of magnetic stripe Track-1 and Track-2 payload data via covert magnetic read-heads, which is subsequently cloned onto counterfeit white plastic cards for fraudulent ATM withdrawals.")
    add_p(doc, "2. PIN Credential Brute-Forcing: Automated or manual dictionary attacks attempted at terminals where adversaries systematically guess PIN sequences for compromised card data lacking PIN records.")
    add_p(doc, "3. High-Velocity Cash-Out Attacks: Coordinated multi-terminal withdrawal campaigns where money mules drain card balance limits across multiple geographic ATMs within very narrow time intervals.")
    add_p(doc, "4. Impossible Geographic Travel (Geo-Velocity Anomaly): Transactions appearing from two distinct geographic terminal locations separated by thousands of kilometers within a time window that violates physical travel possibilities.")
    add_p(doc, "5. Nocturnal Skimming Exploitation: High-value withdrawals initiated during early morning hours (00:00 to 05:00) when legitimate consumers are asleep, reducing the likelihood of immediate victim discovery.")
    add_p(doc, "6. Post-Expiration & Dormant Account Exploitation: Adversarial attempts to authorize transactions against compromised card numbers that have been cancelled, expired, or administratively frozen.")

    add_sec_heading(doc, "1.4 Problem Statement")
    add_p(doc, "The fundamental technical challenge addressed in this work is the rapid, highly accurate identification and interception of fraudulent ATM card transactions within continuous, high-throughput financial data streams without disrupting genuine cardholders. Specifically, this challenge is defined by four core engineering barriers:")
    add_p(doc, "1. Extreme Class Imbalance & The Accuracy Paradox: In real-world enterprise banking transaction logs, fraudulent incidents represent an infinitesimal fraction of overall traffic—typically fewer than 0.1% to 0.4% of total events. When standard machine learning classification algorithms (such as unweighted Decision Trees, Support Vector Machines, or Logistic Regression) are trained on such skewed distributions, their objective functions optimize for overall nominal accuracy by learning to predict the majority non-fraudulent class unconditionally. A naive classifier predicting 'Legitimate' for every single transaction achieves a deceptive nominal accuracy exceeding 99.6%, yet detects exactly zero fraudulent attacks. This phenomenon, known in computer science as the Accuracy Paradox, creates a perilous illusion of security while leaving financial reserves completely unprotected.")
    add_p(doc, "2. Operational Rigidity and High False-Positive Alarms: Conventional financial rule engines rely upon fixed, deterministic conditional thresholds (e.g., 'flag if withdrawal amount > $1,000' or 'block card if 3 consecutive PIN retries fail'). While deterministic rules prevent rudimentary mistakes, they are inherently brittle against adaptive adversaries who calibrate withdrawal amounts just below the threshold. Furthermore, rigid rules generate excessive false-positive alarms—freezing legitimate cards when customers travel or make seasonal purchases—which degrades user experience and overwhelms customer support desks.")
    add_p(doc, "3. Sub-100 Millisecond Latency Constraints: ATM host switches operate under strict operational latency service level agreements (SLAs), requiring authorization decisions to be rendered within 100 to 150 milliseconds. Complex deep neural architectures or distributed database queries across historical ledgers often introduce prohibitive computational overhead, leading to system timeouts or forced fallbacks to insecure bypass modes.")
    add_p(doc, "4. Explainability and Regulatory Compliance: Modern legal frameworks, including the EU General Data Protection Regulation (GDPR Article 22) and the US Fair Credit Reporting Act, require financial institutions to provide actionable explanations when an automated decision blocks a consumer's account. Black-box machine learning models that output raw uncalibrated probabilities fail to meet this legal standard.")

    add_sec_heading(doc, "1.5 Project Objectives & Success Criteria")
    add_p(doc, "To resolve these systemic dilemmas, the primary aim of the CardShield project is to design, implement, and benchmark an intelligent, high-throughput, multi-tier ATM card fraud detection and risk prevention platform. The specific operational and engineering objectives are:")
    add_p(doc, "• Formulate and train a cost-sensitive Balanced Random Forest machine learning classifier that penalizes minority fraud misclassifications, eliminating the Accuracy Paradox and optimizing for high Fraud Recall (TPR) and ROC-AUC rather than raw nominal accuracy.")
    add_p(doc, "• Engineer an intelligent 7-dimensional behavioral risk heuristic engine that evaluates contextual transaction features: inter-transaction velocity, geographical velocity (impossible travel), consecutive PIN failure streaks, midnight transaction anomalies, account status checks, and card tier multipliers.")
    add_p(doc, "• Implement deterministic critical safety clamping mechanisms ensuring that extreme high-risk conditions (e.g., transactions attempted on blocked accounts or expired card credentials) are instantly clamped to a Risk Score of 100, overriding statistical inference.")
    add_p(doc, "• Develop a sub-100ms lightweight Python Flask RESTful API capable of performing feature transformation, model inference, dynamic risk aggregation, and automated account lockdown execution.")
    add_p(doc, "• Construct an interactive cyber defense operations console featuring live transaction streaming, dynamic visual threat meters, automated modal incident dispatch, and forensic audit timeline logs.")

    add_sec_heading(doc, "1.6 Scope and Limitations of the Study")
    add_p(doc, "The scope of this project encompasses the design of the synthetic transaction generator reflecting realistic banking distributions, feature engineering and encoding pipelines, cost-sensitive model training, REST API endpoint implementation, and full-stack client visualization. The system is designed to simulate ATM terminal network switches and provide cyber defense analysts with automated risk scores and instant emergency controls.")
    add_p(doc, "Limitations of the current scope include reliance on simulated transactional datasets due to stringent global banking privacy regulations (such as GDPR and PCI-DSS) that prohibit the public sharing of un-anonymized live cardholder transaction streams. Furthermore, the geographical velocity verification currently assumes two-point terminal distance estimates rather than real-time cellular triangulation.")

    add_sec_heading(doc, "1.7 System Requirements & Operational Assumptions")
    add_p(doc, "The CardShield platform is engineered to operate under typical commercial banking network constraints. Functional requirements stipulate that every transaction request must be validated against schema constraints, mapped to an authorized cardholder profile, scored across statistical and behavioral pipelines, and assigned an immutable audit identifier. Non-functional requirements mandate that the mean end-to-end processing latency shall not exceed 100 milliseconds under a concurrent load of 500 requests per second, with system uptime exceeding 99.99%. It is assumed that ATM terminals communicate over secure virtual private networks (VPNs) and that core account status tables are accessible via local low-latency cache stores.")

    add_sec_heading(doc, "1.8 Organization of the Report")
    add_p(doc, "The remainder of this report is organized as follows: Chapter 2 provides an exhaustive literature survey reviewing existing fraud detection paradigms, machine learning models, and rule-based limitations. Chapter 3 details the proposed CardShield system architecture, execution pipelines, data flow diagrams, and the mathematical formulation of the 7-factor behavioral risk engine. Chapter 4 describes the methodology, feature engineering, software/hardware environments, and security protocols. Chapter 5 presents empirical results, confusion matrices, ROC-AUC curves, dashboard outputs, and comparative benchmarks. Chapter 6 concludes the report and identifies directions for future enhancement, followed by References and Appendices.")

    doc.add_page_break()

    # =========================================================
    # CHAPTER 2: LITERATURE SURVEY
    # =========================================================
    add_chapter_title(doc, "Chapter 2", "Literature Survey")

    add_sec_heading(doc, "2.1 Literature Review & Historical Evolution of Financial Fraud Detection")
    add_p(doc, "Automated fraud detection in payment systems has been a critical subject of academic and commercial inquiry for more than three decades. In early financial computing architectures, fraud mitigation was treated primarily as an accounting reconciliation task. Banks performed end-of-day batch processing to identify discrepancies between ledger entries and physical cash reserves. As electronic fund transfers and ATM networks emerged in the 1980s and 1990s, the paradigm shifted toward real-time authorization switches.")
    add_p(doc, "Early computerized systems introduced Expert Systems based on production rules. In these architectures, human domain experts and forensic auditors authored hundreds of heuristic 'IF-THEN' clauses. For example, if a transaction occurred outside a cardholder's home state and exceeded 80% of the daily withdrawal limit, the system flagged the record for manual operator inspection. Seminal research by Ghosh and Reilly (1994) demonstrated that while expert systems succeeded in intercepting coarse fraud, their maintenance overhead scaled exponentially with transaction volume, and they suffered catastrophic vulnerability to zero-day attack patterns.")
    add_p(doc, "With the exponential increase in computing power and algorithmic maturation in the 2000s, machine learning emerged as the dominant paradigm. Researchers began investigating neural networks, Support Vector Machines (SVMs), decision trees, and Bayesian networks to extract statistical boundaries between genuine cardholder behavior and fraudulent intrusions. Recent studies by Dal Pozzolo et al. (2015) emphasized the concept drift inherent in financial streams: cardholder spending habits change across holiday seasons, while fraudsters continuously alter their techniques to bypass established classifiers.")
    add_p(doc, "Bhattacharyya et al. (2011) conducted an extensive comparative benchmark of data mining techniques on credit card transaction streams, evaluating Support Vector Machines, Random Forests, and Logistic Regression. Their empirical findings confirmed that ensemble tree methods—particularly Random Forests—consistently outperformed individual parametric classifiers due to their resilience to feature collinearity and ability to construct non-linear decision boundaries. However, their study also revealed that standard ensemble models degraded rapidly when minority class representation dropped below 1%, underscoring the absolute necessity of algorithmic cost reweighting.")
    add_p(doc, "Bolton and Hand (2002) surveyed statistical methods for fraud detection, classifying methodologies into supervised fraud profiling and unsupervised peer-group analysis. Supervised models evaluate transaction features against known attack signatures, whereas unsupervised methods compute statistical break-point analysis to detect abrupt shifts in cardholder behavior over temporal windows. They concluded that purely unsupervised techniques, while valuable for novel anomaly discovery, generate excessive false-positive rates that disrupt legitimate banking consumers, recommending hybrid frameworks that synthesize statistical pattern recognition with contextual domain rules.")

    add_sec_heading(doc, "2.2 Survey of Supervised Learning Algorithms")
    add_p(doc, "Supervised machine learning operates under the assumption that a corpus of historical transactions exists wherein each record is mapped to a ground-truth label y in {0, 1}, where 0 denotes legitimate traffic and 1 represents confirmed fraud. Key supervised architectures explored in financial cybersecurity literature include:")
    add_p(doc, "• Logistic Regression: A generalized linear model that maps feature combinations to probability space via the logistic sigmoid function sigma(z) = 1 / (1 + e^(-z)). While computationally trivial (inference latency < 1 millisecond) and highly interpretable, Logistic Regression assumes linear separability in the log-odds space, rendering it fundamentally incapable of capturing complex interaction terms (e.g., the non-linear interaction between late-night hours and consecutive PIN failure counts) without manual feature engineering.")
    add_p(doc, "• Support Vector Machines (SVM): Constructs an optimal separating hyperplane maximizing the geometric margin between classes in high-dimensional Hilbert space via kernel transformations (Radial Basis Function - RBF). SVMs exhibit strong theoretical generalization bounds. However, training complexity scales quadratically with dataset size O(N^2 to N^3), making SVMs computationally intractable for massive enterprise transaction streams.")
    add_p(doc, "• Decision Trees & Random Forests: Decision trees partition the feature space into hyper-rectangles by recursively minimizing Gini impurity or Shannon entropy. While individual trees suffer from high variance and susceptibility to overfitting, Breiman's Random Forest algorithm (2001) resolves this limitation by constructing an ensemble of decorrelated decision trees trained on bootstrap samples with random feature subsets. Random Forests provide superior robustness against outliers, handle non-linear feature interactions seamlessly, and exhibit sub-10ms inference latencies, making them the optimal algorithmic core for CardShield.")

    add_sec_heading(doc, "2.3 Survey of Unsupervised Anomaly Detection Algorithms")
    add_p(doc, "Unsupervised anomaly detection algorithms operate without explicit fraud labels, attempting to model the normal operational manifold of cardholder transactions and tagging outliers that fall in sparse density regions:")
    add_p(doc, "• Isolation Forests: Developed by Liu, Ting, and Zhou (2008), Isolation Forests isolate anomalies by recursively selecting random features and random split values. Because anomalies are few and attribute-wise disparate, they are isolated much closer to the root of the isolation trees than normal instances. While highly efficient for streaming data, Isolation Forests struggle with hyper-dimensional boundary drift and lack calibrated class probabilities.")
    add_p(doc, "• Autoencoders: Deep neural autoencoders compress transaction feature vectors into a narrow latent bottleneck before reconstructing the original input. The reconstruction error (MSE) serves as an anomaly score. However, autoencoder training requires substantial computational resources, and their high inference latency (> 50ms on CPU) hinders real-time ATM switch integration.")

    add_sec_heading(doc, "2.4 Resampling vs. Cost-Sensitive Approaches for Imbalanced Datasets")
    add_p(doc, "To mitigate severe class imbalance, researchers historically utilized data-level resampling techniques, such as Random Undersampling (RUS), Random Oversampling (ROS), Synthetic Minority Over-sampling Technique (SMOTE), and Adaptive Synthetic (ADASYN):")
    add_p(doc, "• Synthetic Minority Over-sampling Technique (SMOTE): Formulated by Chawla et al. (2002), SMOTE synthesizes artificial minority instances along the line segments connecting k-nearest neighbors in Euclidean feature space. While effective for static benchmarking, SMOTE introduces artificial points into high-density regions, alters true probability calibration, and scales poorly in real-time streaming architectures where models must be incrementally updated.")
    add_p(doc, "• Cost-Sensitive Learning: Rather than perturbing dataset distributions, cost-sensitive learning modifies the objective optimization function. A higher misclassification cost is assigned to the minority class (Fraud), forcing the algorithm to penalize false negatives far more severely than false positives. CardShield implements cost-sensitive balanced random forests, ensuring true underlying data integrity while maximizing minority class recall.")

    add_sec_heading(doc, "2.5 Existing Rule-Based Systems & Their Critical Limitations")
    add_p(doc, "A critical analysis of existing enterprise and academic fraud mitigation platforms reveals significant architectural vulnerabilities:")
    add_p(doc, "1. Latency Bottlenecks: Many deep learning approaches (such as Recurrent Neural Networks and LSTMs) evaluate extensive historical transaction sequences. While sequence modeling captures temporal dependencies, the inference latency often exceeds 300 to 500 milliseconds, violating ATM host switch authorization time-out budgets.")
    add_p(doc, "2. Lack of Explainability: Deep black-box neural networks produce uncalibrated probability scores without transparent causal explanations. Global regulatory frameworks, such as the Fair Credit Reporting Act and EU-GDPR Article 22, legally mandate that financial institutions provide actionable explanations when an adverse credit or account blocking decision is rendered. Rule-less neural architectures fail this compliance requirement.")
    add_p(doc, "3. Disconnected Behavioral Context: Many models evaluate the transaction in isolation, looking only at the dollar amount and merchant category code. They omit vital temporal context, such as how many seconds elapsed since the prior transaction, whether the cardholder could physically travel between consecutive terminal locations, or whether previous PIN attempts failed.")

    add_sec_heading(doc, "2.6 The Accuracy Paradox: Formal Mathematical Formulation")
    add_p(doc, "The Accuracy Paradox represents one of the most perilous traps in machine-learning-driven cybersecurity. In typical banking datasets, the distribution of transactions is severely asymmetric: 99.8% of transactions are legitimate, while only 0.2% represent actual fraud. If an unweighted objective function such as Mean Squared Error or standard Binary Cross-Entropy is minimized without cost penalties, the classifier discovers that the easiest mathematical path to minimizing loss is to predict the majority class unconditionally.")
    add_p(doc, "Under this degenerate condition: Nominal Accuracy = (9,980 Legitimate Correct + 0 Fraud Correct) / 10,000 Total = 99.8%. However, the Fraud Recall is exactly 0.0%. In a banking environment processing $50 million daily, this naive model allows 100% of cyber thefts to succeed unnoticed while proudly reporting a 99.8% accuracy score. To overcome this fatal pitfall, CardShield abandons raw nominal accuracy as an optimization metric, adopting Cost-Sensitive Balanced Learning and evaluating performance via ROC-AUC, Precision-Recall curves, and Fraud Recall.")

    add_sec_heading(doc, "2.7 Comparative Matrix of Contemporary Approaches")
    add_p(doc, "Table 2.1 summarizes contemporary fraud detection methodologies, contrasting their algorithmic paradigms, detection mechanisms, latency profiles, and operational drawbacks.")

    # Table 2.1
    p_t21 = doc.add_paragraph()
    p_t21.paragraph_format.space_before = Pt(8)
    p_t21.paragraph_format.space_after = Pt(4)
    r_t21 = p_t21.add_run("Table 2.1: Comparative Analysis of Contemporary ATM Fraud Detection Systems")
    r_t21.bold = True
    r_t21.font.name = 'Times New Roman'
    r_t21.font.size = Pt(11)

    t21 = doc.add_table(rows=1, cols=5)
    t21.alignment = WD_TABLE_ALIGNMENT.CENTER
    t21.autofit = False
    set_table_borders(t21, color="7F8C8D", sz="4")

    headers_21 = ["System / Model", "Core Technique", "Latency", "Fraud Recall", "Operational Limitations"]
    widths_21 = [Inches(1.2), Inches(1.2), Inches(0.8), Inches(0.9), Inches(2.1)]
    for i, c in enumerate(t21.rows[0].cells):
        c.width = widths_21[i]
        set_cell_background(c, "EAECEE")
        set_cell_margins(c, top=100, bottom=100, left=80, right=80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(headers_21[i])
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    rows_21 = [
        ("Static Rule Engines", "Heuristic Thresholds", "< 25 ms", "35 - 45%", "Inflexible; high false positives; easily circumvented by botnets."),
        ("One-Class SVM", "Unsupervised Outliers", "120 - 180 ms", "55 - 65%", "Severe false alarm rate; struggles with seasonal spending shifts."),
        ("LSTM Neural Nets", "Deep Temporal RNN", "350 - 550 ms", "72 - 80%", "Exceeds ATM latency SLAs; complete lack of explainability."),
        ("Standard RF (Raw)", "Unweighted Ensemble", "< 60 ms", "15 - 25%", "Victim of Accuracy Paradox; ignores minority fraud class."),
        ("CardShield (Proposed)", "Balanced RF + 7-Factor Behavioral Engine", "< 85 ms", "78.4% (86.5% ROC)", "Hybrid defense; sub-100ms latency; zero-day safety clamping.")
    ]

    for row_data in rows_21:
        row = t21.add_row()
        for i, val in enumerate(row_data):
            c = row.cells[i]
            c.width = widths_21[i]
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [2, 3] else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            if i == 4 and "CardShield" in row_data[0]:
                set_cell_background(c, "E8F8F5")

    doc.add_page_break()

    # =========================================================
    # CHAPTER 3: PROPOSED SYSTEM
    # =========================================================
    add_chapter_title(doc, "Chapter 3", "Proposed System")

    add_sec_heading(doc, "3.1 Proposed System Overview & Defense-in-Depth Paradigm")
    add_p(doc, "CardShield is designed upon a multi-tier, defense-in-depth architectural paradigm. Rather than delegating risk authorization entirely to an unverified machine learning score or an inflexible set of legacy rules, CardShield synthesizes machine intelligence, dynamic behavioral analytics, and deterministic emergency boundaries into a unified security pipeline.")
    add_p(doc, "The defense-in-depth philosophy recognizes that in cybersecurity, no single layer is infallible. Machine learning algorithms provide remarkable pattern recognition across multidimensional vectors, yet they can be tricked by adversarial edge cases or unobserved data shifts. Conversely, heuristic rules provide guaranteed protection against known policy violations (such as transacting on a reported stolen card), yet they fail against complex behavioral fraud. By ensembling both paradigms, CardShield establishes a resilient, fail-safe security posture.")
    add_p(doc, "The system architecture is structured across four decoupled operational tiers:")
    add_p(doc, "1. Presentation & Operations Console Tier: Constructed using lightweight HTML5, responsive CSS3 grids, and asynchronous JavaScript (AJAX/Fetch). It delivers real-time transaction streaming, dynamic SVG risk meters, automated modal incident dispatch, and a comprehensive forensic audit ledger.")
    add_p(doc, "2. API Gateway & Controller Tier: Powered by Python Flask and Werkzeug, this tier provides RESTful endpoints (`/predict`, `/status`, `/logs`), parses incoming JSON transaction payloads, manages CORS security headers, and orchestrates downstream processing pipelines.")
    add_p(doc, "3. Machine Learning Inference Tier: Houses the serialized, cost-sensitive Balanced Random Forest classifier (`model.joblib`), which evaluates standardized feature vectors and generates a calibrated statistical fraud probability P(Fraud).")
    add_p(doc, "4. 7-Factor Behavioral Risk Engine: Computes a multi-dimensional risk index across velocity, geographic displacement, PIN attempt streaks, temporal hour, card status, and card tier. It applies deterministic risk clamping when critical account violations occur.")

    add_fig(doc, "report_images/fig_system_architecture.png", "Figure 3.1: CardShield Multi-Tier Architecture & Data Exchange Pipeline", width_in=5.6)

    add_sec_heading(doc, "3.2 System Working Description & Execution Pipeline")
    add_p(doc, "When an ATM transaction request is initiated at a remote terminal, the authorization payload is transmitted to the CardShield API endpoint (`/predict`). The transaction lifecycle proceeds through the following sequential stages:")
    add_p(doc, "• Step 1: Payload Parsing & Sanity Validation: The JSON payload is validated for required parameters (Card ID, Amount, Inter-Transaction Duration, PIN Failure Count, Previous Location, Current Location, Transaction Hour, Card Type, and Account Status). Missing or malformed keys trigger immediate HTTP 400 validation rejections.")
    add_p(doc, "• Step 2: Categorical Encoding: The categorical card tier strings ('debit', 'credit-classic', 'credit-gold', 'credit-platinum') are mapped to ordinal integer representations recognized by the underlying machine learning model.")
    add_p(doc, "• Step 3: Statistical Inference: The 5-dimensional feature vector is passed to the Balanced Random Forest model. The model computes the tree voting consensus, outputting the class probability P(Fraud) between 0.0 and 1.0.")
    add_p(doc, "• Step 4: Behavioral Context Evaluation: Concurrently, the 7-factor behavioral engine calculates dynamic penalty points based on real-time context (e.g., rapid consecutive transactions, PIN brute-forcing, high withdrawal amounts).")
    add_p(doc, "• Step 5: Critical Risk Clamping: If the card status is flagged as 'blocked' or 'expired', the system bypasses statistical aggregation and immediately clamps the final Risk Score to 100.")
    add_p(doc, "• Step 6: Enforcement & Response Dispatch: If the aggregated Risk Score exceeds the critical threshold (Score >= 70), the transaction is automatically declined, the card is locked down in the database, and an alert is broadcast to the security operations center within 85 milliseconds.")

    add_sec_heading(doc, "3.3 Flowchart / Data Flow Diagrams (DFD Level 0 & Level 1)")
    add_p(doc, "To provide complete architectural transparency, the system data transformations are formally specified via Data Flow Diagrams. In DFD Level 0 (Context Level), external ATM terminals interact directly with the CardShield Core Engine, exchanging raw transaction requests for signed authorization verdicts.")
    add_p(doc, "Figure 3.2 illustrates the DFD Level 1 architecture, decomposing the core processing block into distinct sub-processes: Input Validation & Feature Extraction (Process 1.0), ML Random Forest Inference (Process 2.0), 7-Factor Behavioral Risk Engine (Process 3.0), and Ensemble & Enforcement Action (Process 4.0).")

    add_fig(doc, "report_images/fig_data_flow_diagram.png", "Figure 3.2: CardShield Data Flow Diagram (DFD Level 1 Context Architecture)", width_in=5.6)

    add_sec_heading(doc, "3.4 7-Factor Behavioral Risk Engine Mathematical Formulation")
    add_p(doc, "The CardShield Behavioral Risk Engine operates as an ensemble function that synthesizes the machine learning probability P(Fraud) with a dynamic penalty accumulator S_behav. The total composite Risk Score R_total in the range [0, 100] is defined mathematically by:")
    add_p(doc, "R_total = min( 100, max( 0, [ alpha * (P(Fraud) * 100) + (1 - alpha) * S_behav ] ) )")
    add_p(doc, "where alpha = 0.50 denotes the balanced ensemble weight, and S_behav represents the linear summation of the seven contextual risk components:")
    add_p(doc, "S_behav = sum( W_i * f_i(x) ) for i = 1 to 7")
    add_p(doc, "The individual behavioral risk factors and their assigned weights are formulated as follows:")
    add_p(doc, "1. Card Status Penalty (W1 = 35%): Evaluates account legitimacy. If Card Status = 'blocked' or 'expired', f_1(x) = 1.0, triggering critical risk clamping where R_total = 100 unconditionally.")
    add_p(doc, "2. Consecutive PIN Retry Failures (W2 = 25%): Models brute-force attack attempts. If PIN Failures >= 3, f_2(x) = 1.0; if PIN Failures == 2, f_2(x) = 0.6; if PIN Failures == 1, f_2(x) = 0.2.")
    add_p(doc, "3. High Velocity / Duration Decay (W3 = 15%): Models rapid automated withdrawals. If Duration < 60 seconds since the prior withdrawal, f_3(x) = 1.0; if Duration < 300 seconds, f_3(x) = 0.5.")
    add_p(doc, "4. Geographical Jump Velocity (W4 = 12%): Detects impossible physical travel. If Terminal Location != Previous Location while Duration < 1,800 seconds (30 mins), f_4(x) = 1.0.")
    add_p(doc, "5. Transaction Amount Anomaly (W5 = 8%): Compares withdrawal amount against tier baseline averages. If Amount > 3 * Baseline, f_5(x) = 1.0.")
    add_p(doc, "6. Nocturnal Midnight Hour (W6 = 3%): Evaluates transaction timing. If Hour in [00:00, 05:00], f_6(x) = 1.0, reflecting historical high-risk skimming hours.")
    add_p(doc, "7. Card Tier Multiplier (W7 = 2%): Adjusts risk sensitivity based on card tier limits (Platinum > Gold > Classic > Debit).")

    add_fig(doc, "report_images/fig_risk_weights.png", "Figure 3.3: CardShield 7-Factor Behavioral Risk Engine Contribution Breakdown", width_in=5.4)

    add_sec_heading(doc, "3.5 Account Lockdown & Risk Threshold Policy Enforcement")
    add_p(doc, "To translate continuous risk scores into decisive banking operational actions, CardShield establishes a three-tier enforcement policy:")
    add_p(doc, "• Low Risk (0 - 39): Transaction is authorized seamlessly. Normal terminal receipt is dispensed. Latency overhead is minimized to under 60 milliseconds.")
    add_p(doc, "• Medium Suspicion (40 - 69): Transaction is flagged for Step-Up Multi-Factor Authentication. The ATM terminal prompts the user for an Out-of-Band (OOB) OTP confirmation sent to their registered mobile device.")
    add_p(doc, "• High Critical Fraud (70 - 100): Transaction is instantly rejected. The card record is shifted to 'Blocked' status in the core banking database, preventing subsequent drain attacks. An automated high-priority incident alert is pushed to the security operations center console.")

    doc.add_page_break()
    print("Exhaustive Chapters 1 to 3 written successfully.")

if __name__ == '__main__':
    doc = Document()
    add_chapters_1_to_3(doc)
    doc.save("test_ch13_exh.docx")
    print("Test exhaustive chapters 1 to 3 saved.")
