# -*- coding: utf-8 -*-
"""
Deeply Aligned Chapters 1 to 3 generation for CardShield Academic Project Report
100% matched to PPT Card Shiels.pptx, app.py, and app.js.
"""

import os
from docx.shared import Inches, Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from generate_all import set_cell_background, set_cell_margins, set_table_borders

def add_p(doc, text, indent=True, space_after=4):
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

def add_chapter_title(doc, chap_num_str, title_str, page_break=True):
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.line_spacing = 1.5
    p1.paragraph_format.space_before = Pt(12)
    p1.paragraph_format.space_after = Pt(2)
    if page_break:
        p1.paragraph_format.page_break_before = True
    run1 = p1.add_run(chap_num_str.upper())
    run1.bold = True
    run1.font.name = 'Times New Roman'
    run1.font.size = Pt(14)
    
    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.line_spacing = 1.5
    p2.paragraph_format.space_before = Pt(0)
    p2.paragraph_format.space_after = Pt(14)
    p2.paragraph_format.keep_with_next = True
    run2 = p2.add_run(title_str.upper())
    run2.bold = True
    run2.font.name = 'Times New Roman'
    run2.font.size = Pt(14)

def add_sec_heading(doc, sec_str):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
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
    p.paragraph_format.keep_with_next = True
    run = p.add_run(subsec_str)
    run.bold = True
    run.italic = True
    run.font.name = 'Times New Roman'
    run.font.size = Pt(12)
    return p

def add_fig(doc, img_path, caption_str, width_in=4.6):
    if os.path.exists(img_path):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_before = Pt(8)
        p_img.paragraph_format.space_after = Pt(2)
        p_img.paragraph_format.first_line_indent = Inches(0)
        p_img.paragraph_format.keep_with_next = True
        run_img = p_img.add_run()
        run_img.add_picture(img_path, width=Inches(width_in))
        
        p_cap = doc.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cap.paragraph_format.space_before = Pt(2)
        p_cap.paragraph_format.space_after = Pt(10)
        p_cap.paragraph_format.first_line_indent = Inches(0)
        run_cap = p_cap.add_run(caption_str)
        run_cap.bold = True
        run_cap.font.name = 'Times New Roman'
        run_cap.font.size = Pt(10.5)

def add_chapters_1_to_3(doc):
    # =========================================================
    # CHAPTER 1: INTRODUCTION
    # =========================================================
    add_chapter_title(doc, "Chapter 1", "Introduction")

    add_sec_heading(doc, "1.1 Motivation & Historical Evolution of ATM Banking Fraud")
    add_p(doc, "Over the past four decades, the global financial services landscape has undergone an extraordinary technological revolution. The mechanization and subsequent digitization of financial transactions shifted retail banking from physical brick-and-mortar branches into a ubiquitous, round-the-clock Automated Teller Machine (ATM) and point-of-sale (POS) terminal infrastructure. Modern consumers depend heavily on debit and credit cards for essential cash withdrawals, daily retail procurement, business transactions, and emergency funds. According to reports published by international financial watchdogs and payment card consortiums, billions of electronic card transactions are authorized daily across more than 3.5 million networked ATM terminals worldwide.")
    add_p(doc, "However, this immense transactional velocity and the convenience of distributed banking access have simultaneously transformed payment card infrastructures into the primary target of sophisticated global cybercrime cartels. Financial fraud has evolved from rudimentary, opportunistic purse-snatching into highly organized, automated cyber threats executed by transnational criminal syndicates.")
    add_p(doc, "In the early eras of ATM deployment, attacks were primarily physical, involving safecracking or the physical extraction of the cash dispenser using heavy machinery. As physical security reinforced ATM chassis, adversaries pivoted toward electronic and software exploitation. Criminals began deploying ultra-thin physical skimming modules within ATM card insertion bezels to capture unencrypted magnetic stripe Track-2 data. Concurrently, miniature pinhole cameras and false tactile keypad overlays recorded cardholder Personal Identification Numbers (PINs).")
    add_p(doc, "In recent years, the threat landscape has intensified with the advent of deep-insert skimmers placed directly inside the motorized card reader mechanism, alongside paper-thin microchip bypass 'shimming' devices that intercept communications between the chip and the terminal. These physical-electronic exploits are paired with automated dark-web marketplaces and botnets that execute synchronized cash-out attacks across international boundaries within minutes.")
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

    add_sec_heading(doc, "1.4 Problem Statement & The Accuracy Paradox Challenge")
    add_p(doc, "The fundamental technical challenge addressed in this work is the rapid, highly accurate identification and interception of fraudulent ATM card transactions within continuous, high-throughput financial data streams without disrupting genuine cardholders. Specifically, this challenge is defined by four core engineering barriers:")
    add_p(doc, "1. Extreme Class Imbalance & The Accuracy Paradox: In real-world enterprise banking transaction logs, fraudulent incidents represent an infinitesimal fraction of overall traffic—typically fewer than 0.1% to 0.5% of total events. When standard machine learning classification algorithms are trained on such skewed distributions without cost-sensitive compensation, their objective functions optimize for overall nominal accuracy by learning to predict the majority non-fraudulent class unconditionally. A naive classifier predicting 'Legitimate' for every single transaction achieves a deceptive nominal accuracy exceeding 99.5%, yet detects exactly zero fraudulent attacks. This phenomenon, known in computer science as the Accuracy Paradox, creates a perilous illusion of security while leaving financial reserves completely unprotected.")
    add_p(doc, "2. Operational Rigidity and High False-Positive Alarms: Conventional financial rule engines rely upon fixed, deterministic conditional thresholds (e.g., 'flag if withdrawal amount > $1,000' or 'block card if 3 consecutive PIN retries fail'). While deterministic rules prevent rudimentary mistakes, they are inherently brittle against adaptive adversaries who calibrate withdrawal amounts just below the threshold. Furthermore, rigid rules generate excessive false-positive alarms—freezing legitimate cards when customers travel or make seasonal purchases—which degrades user experience and overwhelms customer support desks.")
    add_p(doc, "3. Sub-Second Latency Constraints: ATM host switches operate under strict operational latency service level agreements (SLAs), requiring authorization decisions to be rendered in less than one second (ideally < 100 milliseconds). Complex deep neural architectures or distributed database queries across historical ledgers often introduce prohibitive computational overhead, leading to system timeouts or forced fallbacks to insecure bypass modes.")
    add_p(doc, "4. Multi-Factor Context Integration: In isolation, a transaction amount or location may appear completely benign. However, when combined with temporal factors (such as a 3:00 AM transaction hour), high velocity (10+ withdrawals in 24 hours), or high credit limit utilization (> 80%), the composite risk multiplies exponentially.")

    add_sec_heading(doc, "1.5 Project Objectives & Success Criteria")
    add_p(doc, "To resolve these systemic dilemmas, the primary aim of the CardShield project is to design, implement, and benchmark an intelligent, high-throughput, multi-tier ATM card fraud detection and risk prevention platform. The specific operational and engineering objectives are:")
    add_p(doc, "1. Instant Detection: Check every incoming card transaction in less than 1 second (< 85 milliseconds) so that legitimate customer transactions are never delayed.")
    add_p(doc, "2. Catch Real Frauds (Solve Accuracy Paradox): Train a Cost-Sensitive Balanced Random Forest classifier on 100,000 bank transactions that optimizes specifically for minority fraud recall, achieving >= 75% fraud recall and >= 85% ROC-AUC quality score.")
    add_p(doc, "3. Multi-Signal Verification: Evaluate seven distinct contextual dimensions: Card Status, Transaction Amount, Time of Day, Location (Domestic vs International), Merchant Category, Transaction Frequency, and Credit Limit Utilization.")
    add_p(doc, "4. User-Friendly Cyber Defense Console: Build a clean, responsive web dashboard equipped with an animated speedometer risk gauge, real-time telemetry bars, preset test simulation profiles, and an incident audit feed.")
    add_p(doc, "5. Automated Operational Recommendations: Automatically categorize transactions into three actionable risk tiers: Low Risk (0–39, Approve), Medium Risk (40–69, Send Step-Up OTP), and High Risk / Fraud (70–100, Decline & Block Card Immediately).")

    add_sec_heading(doc, "1.6 Work Plan Schedule & Milestone Execution Timeline")
    add_p(doc, "The CardShield project was executed across a structured four-month development lifecycle under the Problem-Based Learning (PBL) curriculum of the BCA program during the Autumn 2026 semester. Table 1.1 documents the month-by-month milestone execution plan.")

    # Table 1.1: Work Plan Schedule (from PPT Slide 8)
    p_t11 = doc.add_paragraph()
    p_t11.paragraph_format.space_before = Pt(8)
    p_t11.paragraph_format.space_after = Pt(4)
    r_t11 = p_t11.add_run("Table 1.1: Work Plan Schedule & Milestone Execution Timeline")
    r_t11.bold = True
    r_t11.font.name = 'Times New Roman'
    r_t11.font.size = Pt(11)

    t11 = doc.add_table(rows=1, cols=5)
    t11.alignment = WD_TABLE_ALIGNMENT.CENTER
    t11.autofit = False
    set_table_borders(t11, color="7F8C8D", sz="4")

    h_11 = ["Project Activity / Milestone", "August 2026", "September 2026", "October 2026", "November 2026"]
    w_11 = [Inches(2.8), Inches(0.9), Inches(1.0), Inches(0.9), Inches(1.0)]
    for i, c in enumerate(t11.rows[0].cells):
        c.width = w_11[i]
        set_cell_background(c, "EAECEE")
        set_cell_margins(c, top=100, bottom=100, left=80, right=80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i > 0 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h_11[i])
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    rows_11 = [
        ("Literature Reviews & Domain Exploration", "Completed", "-", "-", "-"),
        ("Component Identification & Tech Selection", "Completed", "-", "-", "-"),
        ("AI Model Training (Balanced Random Forest)", "-", "Completed", "-", "-"),
        ("Backend Flask Server & REST API Setup", "-", "Completed", "-", "-"),
        ("Frontend UI Designing & Speedometer Gauge", "-", "-", "Completed", "-"),
        ("End-to-End System Testing & Debugging", "-", "-", "Completed", "-"),
        ("Project Report Preparation & Documentation", "-", "-", "Completed", "Final Submission")
    ]

    for row_data in rows_11:
        row = t11.add_row()
        for i, val in enumerate(row_data):
            c = row.cells[i]
            c.width = w_11[i]
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i > 0 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            if val in ["Completed", "Final Submission"]:
                r.bold = True
                if val == "Final Submission":
                    set_cell_background(c, "D5F5E3")

    add_sec_heading(doc, "1.7 Project Deliverables & Academic Submission Specifications")
    add_p(doc, "Table 1.2 details the complete set of academic and engineering deliverables prepared for final project submission, as specified in the project milestone registry.")

    # Table 1.2: Project Deliverables (from PPT Slide 9)
    p_t12 = doc.add_paragraph()
    p_t12.paragraph_format.space_before = Pt(8)
    p_t12.paragraph_format.space_after = Pt(4)
    r_t12 = p_t12.add_run("Table 1.2: Project Deliverables & Academic Submission Specifications")
    r_t12.bold = True
    r_t12.font.name = 'Times New Roman'
    r_t12.font.size = Pt(11)

    t12 = doc.add_table(rows=1, cols=3)
    t12.alignment = WD_TABLE_ALIGNMENT.CENTER
    t12.autofit = False
    set_table_borders(t12, color="7F8C8D", sz="4")

    h_12 = ["Deliverable Item", "Specification / Target", "Verification Status"]
    w_12 = [Inches(2.2), Inches(3.0), Inches(1.4)]
    for i, c in enumerate(t12.rows[0].cells):
        c.width = w_12[i]
        set_cell_background(c, "EAECEE")
        set_cell_margins(c, top=100, bottom=100, left=80, right=80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i == 2 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h_12[i])
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    rows_12 = [
        ("Project Name", "CardShield: Real-Time ATM Card Fraud Detection", "Verified"),
        ("Submission Date", "November 10, 2026", "On Schedule"),
        ("Student Details", "Suryapal Singh | Student ID: 146476 | Roll: 2024COMPSC0029", "Registered"),
        ("Academic Program", "Bachelor of Computer Applications (BCA) – 5th Semester", "Accredited"),
        ("Project Laboratory", "Cognitive Science – Project Based Learning Lab", "Assigned"),
        ("Faculty Mentor", "Prof. Ms. Mohini Fulzele (Assistant Professor)", "Supervised"),
        ("Git Source Code", "GitHub Repository: https://github.com/suryapalsingh8899/Card-Shild", "Deployed"),
        ("Live Cloud Application", "Production Web Service deployed on Render Cloud Platform", "Operational"),
        ("Trained AI Model", "Serialized Random Forest Pipeline: fraud_model.pkl", "Benchmarked"),
        ("Documentation Report", "Comprehensive NIMS Format Academic Project Report (55+ Pages)", "Submitted")
    ]

    for row_data in rows_12:
        row = t12.add_row()
        for i, val in enumerate(row_data):
            c = row.cells[i]
            c.width = w_12[i]
            set_cell_margins(c, top=50, bottom=50, left=80, right=80)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i == 2 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            if i == 0:
                r.bold = True

    add_sec_heading(doc, "1.8 Scope and Limitations of the Study")
    add_p(doc, "The scope of this project encompasses the design of the synthetic transaction generator reflecting realistic banking distributions, feature engineering and encoding pipelines, cost-sensitive model training, REST API endpoint implementation, and full-stack client visualization. The system is designed to simulate ATM terminal network switches and provide cyber defense analysts with automated risk scores and instant emergency controls.")
    add_p(doc, "Limitations of the current scope include reliance on simulated transactional datasets due to stringent global banking privacy regulations (such as GDPR and PCI-DSS) that prohibit the public sharing of un-anonymized live cardholder transaction streams. Furthermore, the geographical velocity verification currently assumes two-point terminal distance estimates rather than real-time cellular triangulation.")

    add_sec_heading(doc, "1.9 Organization of the Report")
    add_p(doc, "The remainder of this report is organized as follows: Chapter 2 provides an exhaustive literature survey reviewing existing fraud detection paradigms, machine learning models, and rule-based limitations. Chapter 3 details the proposed CardShield system architecture, execution pipelines, data flow diagrams, and the mathematical formulation of the 7-factor behavioral risk engine. Chapter 4 describes the methodology, feature engineering, software/hardware environments, and security protocols. Chapter 5 presents empirical results, confusion matrices, ROC-AUC curves, dashboard outputs, and comparative benchmarks. Chapter 6 concludes the report and identifies directions for future enhancement, followed by References and Appendices.")

    # =========================================================
    # CHAPTER 2: LITERATURE SURVEY
    # =========================================================
    add_chapter_title(doc, "Chapter 2", "Literature Survey")

    add_sec_heading(doc, "2.1 Literature Review & Historical Evolution of Fraud Detection")
    add_p(doc, "Automated fraud detection in payment systems has been a critical subject of academic and commercial inquiry for more than three decades. In early financial computing architectures, fraud mitigation was treated primarily as an accounting reconciliation task. Banks performed end-of-day batch processing to identify discrepancies between ledger entries and physical cash reserves. As electronic fund transfers and ATM networks emerged in the 1980s and 1990s, the paradigm shifted toward real-time authorization switches.")
    add_p(doc, "Early computerized systems introduced Expert Systems based on production rules. In these architectures, human domain experts and forensic auditors authored hundreds of heuristic 'IF-THEN' clauses. For example, if a transaction occurred outside a cardholder's home state and exceeded 80% of the daily withdrawal limit, the system flagged the record for manual operator inspection. Seminal research by Ghosh and Reilly (1994) demonstrated that while expert systems succeeded in intercepting coarse fraud, their maintenance overhead scaled exponentially with transaction volume, and they suffered catastrophic vulnerability to zero-day attack patterns.")
    add_p(doc, "With the exponential increase in computing power and algorithmic maturation in the 2000s, machine learning emerged as the dominant paradigm. Researchers began investigating neural networks, Support Vector Machines (SVMs), decision trees, and Bayesian networks to extract statistical boundaries between genuine cardholder behavior and fraudulent intrusions. Recent studies by Dal Pozzolo et al. (2015) emphasized the concept drift inherent in financial streams: cardholder spending habits change across holiday seasons, while fraudsters continuously alter their techniques to bypass established classifiers.")
    add_p(doc, "Bhattacharyya et al. (2011) conducted an extensive comparative benchmark of data mining techniques on credit card transaction streams, evaluating Support Vector Machines, Random Forests, and Logistic Regression. Their empirical findings confirmed that ensemble tree methods—particularly Random Forests—consistently outperformed individual parametric classifiers due to their resilience to feature collinearity and ability to construct non-linear decision boundaries. However, their study also revealed that standard ensemble models degraded rapidly when minority class representation dropped below 1%, underscoring the absolute necessity of algorithmic cost reweighting.")
    add_p(doc, "Bolton and Hand (2002) surveyed statistical methods for fraud detection, classifying methodologies into supervised fraud profiling and unsupervised peer-group analysis. Supervised models evaluate transaction features against known attack signatures, whereas unsupervised methods compute statistical break-point analysis to detect abrupt shifts in cardholder behavior over temporal windows. They concluded that purely unsupervised techniques, while valuable for novel anomaly discovery, generate excessive false-positive rates that disrupt legitimate banking consumers, recommending hybrid frameworks that synthesize statistical pattern recognition with contextual domain rules.")

    add_sec_heading(doc, "2.2 Survey of Supervised & Unsupervised Machine Learning")
    add_p(doc, "Academic literature categorizes machine learning fraud detection systems into three primary methodologies:")
    add_p(doc, "• Supervised Learning Models: In supervised paradigms, algorithms are trained on historical transaction records labeled as either 'Legitimate' (Class 0) or 'Fraudulent' (Class 1). Popular supervised models include Logistic Regression, Artificial Neural Networks (ANN), Random Forests, and Gradient Boosted Decision Trees (XGBoost, LightGBM). Supervised models achieve high precision when ample labeled data is present. However, they struggle when novel fraud typologies appear that were absent from historical training corpora.")
    add_p(doc, "• Unsupervised Anomaly Detection: Unsupervised algorithms operate without explicit ground-truth labels. Techniques such as Isolation Forests, One-Class SVMs, Principal Component Analysis (PCA), and Autoencoders establish a baseline profile of normal customer transactions. Any event that deviates significantly from this manifold is tagged as anomalous. While unsupervised techniques excel at detecting previously unseen zero-day attacks, they historically suffer from high false-positive alarm rates, frequently misidentifying unusual but legitimate customer activities (such as vacation travel) as cyber attacks.")
    add_p(doc, "• Hybrid Ensemble Frameworks: Modern financial security engineering increasingly favors hybrid architectures that ensemble supervised machine learning with domain-specific behavioral heuristics. Ensembling combines the high statistical discriminability of tree-based models with the deterministic safety boundaries of expert heuristic rules. CardShield adopts this hybrid paradigm, coupling a Balanced Random Forest with a 7-factor dynamic behavioral risk scoring engine.")

    add_sec_heading(doc, "2.3 Existing Rule-Based Engines and Their Critical Vulnerabilities")
    add_p(doc, "A critical analysis of existing enterprise and academic fraud mitigation platforms reveals significant architectural vulnerabilities:")
    add_p(doc, "1. Latency Bottlenecks: Many deep learning approaches (such as Recurrent Neural Networks and LSTMs) evaluate extensive historical transaction sequences. While sequence modeling captures temporal dependencies, the inference latency often exceeds 300 to 500 milliseconds, violating ATM host switch authorization time-out budgets.")
    add_p(doc, "2. Lack of Explainability: Deep black-box neural networks produce uncalibrated probability scores without transparent causal explanations. Global regulatory frameworks, such as the Fair Credit Reporting Act and EU-GDPR Article 22, legally mandate that financial institutions provide actionable explanations when an adverse credit or account blocking decision is rendered. Rule-less neural architectures fail this compliance requirement.")
    add_p(doc, "3. Disconnected Behavioral Context: Many models evaluate the transaction in isolation, looking only at the dollar amount and merchant category code. They omit vital temporal context, such as how many seconds elapsed since the prior transaction, whether the cardholder could physically travel between consecutive terminal locations, or whether previous PIN attempts failed.")

    add_sec_heading(doc, "2.4 The Accuracy Paradox: Formal Mathematical Formulation")
    add_p(doc, "The Accuracy Paradox represents one of the most perilous traps in machine-learning-driven cybersecurity. In typical banking datasets, the distribution of transactions is severely asymmetric: 99.8% of transactions are legitimate, while only 0.2% represent actual fraud. If an unweighted objective function such as Mean Squared Error or standard Binary Cross-Entropy is minimized without cost penalties, the classifier discovers that the easiest mathematical path to minimizing loss is to predict the majority class unconditionally.")
    add_p(doc, "Under this degenerate condition: Nominal Accuracy = (9,980 Legitimate Correct + 0 Fraud Correct) / 10,000 Total = 99.8%. However, the Fraud Recall is exactly 0.0%. In a banking environment processing $50 million daily, this naive model allows 100% of cyber thefts to succeed unnoticed while proudly reporting a 99.8% accuracy score. To overcome this fatal pitfall, CardShield abandons raw nominal accuracy as an optimization metric, adopting Cost-Sensitive Balanced Learning and evaluating performance via ROC-AUC, Precision-Recall curves, and Fraud Recall.")

    add_sec_heading(doc, "2.5 Comparative Matrix of Contemporary Approaches")
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

    # =========================================================
    # CHAPTER 3: PROPOSED SYSTEM
    # =========================================================
    add_chapter_title(doc, "Chapter 3", "Proposed System")

    add_sec_heading(doc, "3.1 Proposed System Overview & Defense-in-Depth Topology")
    add_p(doc, "CardShield is designed upon a multi-tier, defense-in-depth architectural paradigm. Rather than delegating risk authorization entirely to an unverified machine learning score or an inflexible set of legacy rules, CardShield synthesizes machine intelligence, dynamic behavioral analytics, and deterministic emergency boundaries into a unified security pipeline.")
    add_p(doc, "The defense-in-depth philosophy recognizes that in cybersecurity, no single layer is infallible. Machine learning algorithms provide remarkable pattern recognition across multidimensional vectors, yet they can be tricked by adversarial edge cases or unobserved data shifts. Conversely, heuristic rules provide guaranteed protection against known policy violations (such as transacting on a reported stolen card), yet they fail against complex behavioral fraud. By ensembling both paradigms, CardShield establishes a resilient, fail-safe security posture.")

    add_sec_heading(doc, "3.2 Multi-Tier System Architecture (UI, Flask, AI Engine)")
    add_p(doc, "The CardShield system architecture is structured across three decoupled, high-performance operational tiers:")
    add_p(doc, "1. Frontend Presentation Tier (app.js & HTML5): Constructed using modern HTML5, responsive CSS3 cyber styling, and vanilla JavaScript (`app.js`). It features an interactive SVG speedometer gauge, 7-factor risk telemetry bars, automated modal alerts, and preconfigured simulation profiles ('Normal Grocery Purchase', 'Midnight ATM Cash Drain', 'Rapid Velocity Attack', 'PIN Brute-Force Sequence').")
    add_p(doc, "2. API Gateway & Controller Tier (app.py): Powered by Python Flask and Werkzeug, this tier provides RESTful endpoints (`/analyze`, `/health`, `/`), parses incoming JSON transaction payloads, maps categorical values to trained encoders, computes behavioral heuristics, and orchestrates ensemble risk fusion.")
    add_p(doc, "3. AI Machine Learning Tier (fraud_model.pkl): Houses the cost-sensitive Balanced Random Forest classifier trained on 100,000 real-world-modeled bank transactions, generating calibrated probability outputs in under 20 milliseconds.")

    add_fig(doc, "report_images/fig_system_architecture.png", "Figure 3.1: CardShield Multi-Tier Architecture & Data Exchange Pipeline", width_in=4.6)

    add_sec_heading(doc, "3.3 System Working Description & Execution Pipeline")
    add_p(doc, "When a transaction is submitted via the operations console or an ATM terminal, the authorization payload is transmitted to the CardShield API endpoint (`POST /analyze`). The transaction lifecycle proceeds through the following sequential stages:")
    add_p(doc, "• Step 1: Payload Parsing & Categorical Normalization: The JSON payload (`txnAmount`, `category`, `cardType`, `cardStatus`, `creditLimit`, `txnLocation`, `txnTime`, `frequency`) is parsed and validated.")
    add_p(doc, "• Step 2: Categorical Feature Encoding: String labels are encoded using Scikit-Learn `LabelEncoder` objects serialized inside `fraud_model.pkl`, safely mapping unseen values to the 'Unknown' class.")
    add_p(doc, "• Step 3: Balanced Random Forest Inference: The 5-dimensional feature vector `[amount, category_enc, type_enc, status_enc, credit_limit]` is evaluated by the Random Forest model, outputting probability P(Fraud).")
    add_p(doc, "• Step 4: Calibrated Statistical Probability Scaling: The raw probability is calibrated into a 0–100 scale: proba <= 0.36 maps to [0–30], proba between 0.36 and 0.50 maps to [30–60], and proba > 0.50 maps to [60–95].")
    add_p(doc, "• Step 5: 7-Dimensional Behavioral Heuristic Scoring: The `compute_heuristic_score()` engine concurrently calculates risk points across the 7 contextual dimensions.")
    add_p(doc, "• Step 6: Ensemble Fusion: The composite risk score is computed: `scaled_score = round(0.40 * ml_score + 0.60 * heuristic_score)`.")
    add_p(doc, "• Step 7: Critical Safety Clamping: If the card is 'Blocked', score is clamped to 98; if 'Expired', score is clamped to 88.")
    add_p(doc, "• Step 8: Action Dispatch: The system returns the risk score, probability, and operational action (< 85ms total latency).")

    add_sec_heading(doc, "3.4 Flowchart / Data Flow Diagrams (DFD Level 0 & Level 1)")
    add_p(doc, "Figure 3.2 illustrates the DFD Level 1 architecture, decomposing the transaction evaluation process into distinct sub-processes: Input Validation & Encoding (Process 1.0), Balanced RF Inference (Process 2.0), 7-Factor Behavioral Scoring (Process 3.0), and Ensemble Fusion & Operational Enforcement (Process 4.0).")

    add_fig(doc, "report_images/fig_data_flow_diagram.png", "Figure 3.2: CardShield Data Flow Diagram (DFD Level 1 Context Architecture)", width_in=4.6)

    add_sec_heading(doc, "3.5 7-Dimensional Behavioral Risk Engine Formulation")
    add_p(doc, "As specified in Slide 4 of the project presentation and implemented in `app.js` and `app.py`, CardShield evaluates seven critical behavioral risk factors totaling exactly 100% contribution weight. Table 3.1 delineates the weight distribution, trigger conditions, and penalty scales.")

    # Table 3.1: 7-Factor Risk Weight Matrix (from PPT Slide 4 & app.js)
    p_t31 = doc.add_paragraph()
    p_t31.paragraph_format.space_before = Pt(8)
    p_t31.paragraph_format.space_after = Pt(4)
    r_t31 = p_t31.add_run("Table 3.1: CardShield 7-Dimensional Behavioral Risk Weight Matrix")
    r_t31.bold = True
    r_t31.font.name = 'Times New Roman'
    r_t31.font.size = Pt(11)

    t31 = doc.add_table(rows=1, cols=4)
    t31.alignment = WD_TABLE_ALIGNMENT.CENTER
    t31.autofit = False
    set_table_borders(t31, color="7F8C8D", sz="4")

    h_31 = ["Risk Dimension", "Weight (%)", "Evaluation Criteria & Trigger Logic", "Dynamic Penalty"]
    w_31 = [Inches(1.8), Inches(0.9), Inches(2.6), Inches(1.3)]
    for i, c in enumerate(t31.rows[0].cells):
        c.width = w_31[i]
        set_cell_background(c, "EAECEE")
        set_cell_margins(c, top=100, bottom=100, left=80, right=80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i == 1 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h_31[i])
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    rows_31 = [
        ("Card Status", "25%", "Active (+2) | Expired (+35) | Blocked (Instant 98 Critical Clamp)", "Up to 98 pts"),
        ("Transaction Amount", "20%", "Deviation vs. legit baseline ($1,850.45). Micro-probe (< $100): +8, High deviation: +10 to +24", "Up to 24 pts"),
        ("Time of Day", "15%", "Nocturnal off-hours: Midnight to 4:00 AM (+18), 4:00 to 7:00 AM (+10), Daytime (+2)", "Up to 18 pts"),
        ("Transaction Location", "15%", "Cross-border / international terminal (+18) vs. Domestic terminal (+2)", "Up to 18 pts"),
        ("Merchant Category", "10%", "Category empirical fraud probability (ATM Withdrawal: 0.523, Shopping: 0.489)", "Up to 10 pts"),
        ("Transaction Frequency", "10%", "24h Velocity spike: <= 3 txns (+2), 4-6 (+6), 7-10 (+14), > 10 rapid transactions (+22)", "Up to 22 pts"),
        ("Credit Limit Utilization", "5%", "Transaction Amount / Credit Limit ratio: > 50% (+5), > 80% (+10), > 100% (+16)", "Up to 16 pts")
    ]

    for row_data in rows_31:
        row = t31.add_row()
        for i, val in enumerate(row_data):
            c = row.cells[i]
            c.width = w_31[i]
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i == 1 else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            if i == 0:
                r.bold = True

    add_fig(doc, "report_images/fig_risk_weights.png", "Figure 3.3: CardShield 7-Dimensional Behavioral Risk Engine Weights (Sum = 100%)", width_in=4.5)

    add_sec_heading(doc, "3.6 Decision Risk Levels & Automated Operational Responses")
    add_p(doc, "To provide clear, actionable operational instructions for bank officers and ATM terminal switches, CardShield maps composite risk scores (0 to 100) into three structured operational tiers (matching Slide 6 of the project presentation). Table 3.2 outlines the operational actions and visual indicator badges.")

    # Table 3.2: Risk Levels (from PPT Slide 6)
    p_t32 = doc.add_paragraph()
    p_t32.paragraph_format.space_before = Pt(8)
    p_t32.paragraph_format.space_after = Pt(4)
    r_t32 = p_t32.add_run("Table 3.2: Decision Risk Levels & Automated Operational Responses")
    r_t32.bold = True
    r_t32.font.name = 'Times New Roman'
    r_t32.font.size = Pt(11)

    t32 = doc.add_table(rows=1, cols=4)
    t32.alignment = WD_TABLE_ALIGNMENT.CENTER
    t32.autofit = False
    set_table_borders(t32, color="7F8C8D", sz="4")

    h_32 = ["Risk Level", "Score Range", "Operational Recommendation", "System Action Executed"]
    w_32 = [Inches(1.5), Inches(1.0), Inches(2.2), Inches(1.9)]
    for i, c in enumerate(t32.rows[0].cells):
        c.width = w_32[i]
        set_cell_background(c, "EAECEE")
        set_cell_margins(c, top=100, bottom=100, left=80, right=80)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 1] else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(h_32[i])
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(10)

    rows_32 = [
        ("🟢 Very Low / Low Risk", "0 – 39", "Safe to Approve", "Authorize transaction immediately; dispense cash / print receipt."),
        ("🟡 Medium Risk", "40 – 69", "Suspicious – Send OTP", "Trigger Step-Up Out-of-Band (OOB) OTP to cardholder mobile device."),
        ("🔴 High Risk / Fraud", "70 – 100", "Fraud Detected – Block Card", "Decline transaction immediately; freeze card account; alert SOC.")
    ]

    for row_data in rows_32:
        row = t32.add_row()
        for i, val in enumerate(row_data):
            c = row.cells[i]
            c.width = w_32[i]
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if i in [0, 1] else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(9.5)
            if i == 0:
                r.bold = True

    print("Updated Chapters 1 to 3 written successfully.")

if __name__ == '__main__':
    doc = Document()
    add_chapters_1_to_3(doc)
    doc.save("test_ch13_matched.docx")
    print("Test updated chapters 1 to 3 saved.")
