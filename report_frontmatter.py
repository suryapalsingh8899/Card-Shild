# -*- coding: utf-8 -*-
"""
Front matter generation for NIMS University Academic Project Report
Matches exact layout from BE_Project_Report_front page _Format1.doc
and 100% aligned with PPT Card Shiels.pptx and CardShield project codebase.
"""

import os
from docx.shared import Inches, Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from generate_all import set_cell_background, set_cell_margins, set_table_borders

def add_frontmatter(doc):
    logo_path = 'report_images/image3.jpg'
    if not os.path.exists(logo_path):
        logo_path = 'nims_logo.jpg'
        
    # =========================================================
    # 1. COVER PAGE (Specimen Format from sample doc)
    # =========================================================
    p_top = doc.add_paragraph()
    p_top.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_top.paragraph_format.space_before = Pt(0)
    p_top.paragraph_format.space_after = Pt(2)
    r = p_top.add_run("A\nPROJECT REPORT\nON")
    r.bold = True
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)

    # Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(12)
    p_title.paragraph_format.space_after = Pt(20)
    r_title = p_title.add_run("CARDSHIELD: REAL-TIME ATM CARD FRAUD DETECTION & BEHAVIORAL RISK ANALYSIS SYSTEM")
    r_title.bold = True
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(16)

    # Submitted By
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(8)
    p_sub.paragraph_format.space_after = Pt(4)
    r_sub = p_sub.add_run("SUBMITTED BY")
    r_sub.bold = True
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(12)

    # Student details
    p_stu = doc.add_paragraph()
    p_stu.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_stu.paragraph_format.space_before = Pt(2)
    p_stu.paragraph_format.space_after = Pt(16)
    r_stu = p_stu.add_run("Mr. Suryapal Singh                                (Enrollment No. 2024COMPSC0029)\nStudent ID: 146476  |  Branch: BCA – 5th Semester")
    r_stu.bold = True
    r_stu.font.name = 'Times New Roman'
    r_stu.font.size = Pt(12)

    # Under the Guidance of
    p_gui_lbl = doc.add_paragraph()
    p_gui_lbl.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_gui_lbl.paragraph_format.space_before = Pt(6)
    p_gui_lbl.paragraph_format.space_after = Pt(2)
    r_gui_lbl = p_gui_lbl.add_run("UNDER THE GUIDANCE OF")
    r_gui_lbl.bold = True
    r_gui_lbl.font.name = 'Times New Roman'
    r_gui_lbl.font.size = Pt(12)

    p_gui = doc.add_paragraph()
    p_gui.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_gui.paragraph_format.space_before = Pt(2)
    p_gui.paragraph_format.space_after = Pt(14)
    r_gui = p_gui.add_run("Prof. Ms. Mohini Fulzele\n(Assistant Professor)")
    r_gui.bold = True
    r_gui.font.name = 'Times New Roman'
    r_gui.font.size = Pt(12)

    # University Emblem
    if os.path.exists(logo_path):
        p_logo = doc.add_paragraph()
        p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo.paragraph_format.space_before = Pt(4)
        p_logo.paragraph_format.space_after = Pt(12)
        run_logo = p_logo.add_run()
        run_logo.add_picture(logo_path, width=Inches(1.50))

    # University, Lab & Department Details
    p_uni = doc.add_paragraph()
    p_uni.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_uni.paragraph_format.space_before = Pt(4)
    p_uni.paragraph_format.space_after = Pt(0)
    p_uni.paragraph_format.line_spacing = 1.25
    
    r_u0 = p_uni.add_run("COGNITIVE SCIENCE – PROJECT BASED LEARNING LAB\n")
    r_u0.bold = True
    r_u0.font.name = 'Times New Roman'
    r_u0.font.size = Pt(12)
    
    r_u1 = p_uni.add_run("MARIK INSTITUTE OF COMPUTING, ARTIFICIAL INTELLIGENCE,\nROBOTICS & CYBERNETICS\n")
    r_u1.bold = True
    r_u1.font.name = 'Times New Roman'
    r_u1.font.size = Pt(13)
    
    r_u2 = p_uni.add_run("DEPARTMENT OF COMPUTER APPLICATIONS\n")
    r_u2.bold = True
    r_u2.font.name = 'Times New Roman'
    r_u2.font.size = Pt(12)
    
    r_u3 = p_uni.add_run("NIMS UNIVERSITY RAJASTHAN, JAIPUR\nNOVEMBER 2026")
    r_u3.bold = True
    r_u3.font.name = 'Times New Roman'
    r_u3.font.size = Pt(13)

    doc.add_page_break()

    # =========================================================
    # 2. CERTIFICATE PAGE (Specimen Format from sample doc)
    # =========================================================
    p_cert_head = doc.add_paragraph()
    p_cert_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_head.paragraph_format.space_before = Pt(0)
    p_cert_head.paragraph_format.space_after = Pt(4)
    p_cert_head.paragraph_format.line_spacing = 1.25
    
    r_ch0 = p_cert_head.add_run("COGNITIVE SCIENCE – PROJECT BASED LEARNING LAB\n")
    r_ch0.bold = True
    r_ch0.font.name = 'Times New Roman'
    r_ch0.font.size = Pt(12)
    
    r_ch1 = p_cert_head.add_run("MARIK INSTITUTE OF COMPUTING, ARTIFICIAL INTELLIGENCE,\nROBOTICS & CYBERNETICS\n")
    r_ch1.bold = True
    r_ch1.font.name = 'Times New Roman'
    r_ch1.font.size = Pt(13)
    
    r_ch2 = p_cert_head.add_run("DEPARTMENT OF COMPUTER APPLICATIONS\nAcademic Year 2026-27")
    r_ch2.bold = True
    r_ch2.font.name = 'Times New Roman'
    r_ch2.font.size = Pt(12)

    # Logo
    if os.path.exists(logo_path):
        p_logo2 = doc.add_paragraph()
        p_logo2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_logo2.paragraph_format.space_before = Pt(6)
        p_logo2.paragraph_format.space_after = Pt(10)
        run_logo2 = p_logo2.add_run()
        run_logo2.add_picture(logo_path, width=Inches(1.30))

    p_cert_title = doc.add_paragraph()
    p_cert_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cert_title.paragraph_format.space_before = Pt(4)
    p_cert_title.paragraph_format.space_after = Pt(12)
    r_ct = p_cert_title.add_run("CERTIFICATE")
    r_ct.bold = True
    r_ct.font.name = 'Times New Roman'
    r_ct.font.size = Pt(15)

    p_cert_body = doc.add_paragraph()
    p_cert_body.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_cert_body.paragraph_format.line_spacing = 1.5
    p_cert_body.paragraph_format.first_line_indent = Inches(0.5)
    p_cert_body.paragraph_format.space_after = Pt(22)
    r_cb = p_cert_body.add_run(
        'This is to certify that the project entitled "CARDSHIELD: REAL-TIME ATM CARD FRAUD DETECTION & BEHAVIORAL RISK ANALYSIS SYSTEM" '
        'is a record of bonafide work carried out by Mr. Suryapal Singh (Enrollment No. 2024COMPSC0029, Student ID: 146476) under my supervision '
        'and guidance, in partial fulfillment of the requirements for the award of Degree of Bachelor of Computer Applications (BCA) '
        'from NIMS University Rajasthan, Jaipur during the year 2026-27.'
    )
    r_cb.font.name = 'Times New Roman'
    r_cb.font.size = Pt(12)

    # Signature Table (Border-less grid)
    sig_table = doc.add_table(rows=1, cols=2)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    sig_table.autofit = False

    sig_data = [
        [
            ("Date: 10/11/2026\nPlace: Jaipur", WD_ALIGN_PARAGRAPH.LEFT),
            ("Ms. Mohini Fulzele\n(Project Guide & Faculty Mentor)\nAssistant Professor\nDepartment of Computer Applications\nMarik Institute of Computing\nNIMS University Rajasthan, Jaipur", WD_ALIGN_PARAGRAPH.RIGHT)
        ]
    ]

    for r_idx, row in enumerate(sig_data):
        for c_idx, (text, align) in enumerate(row):
            cell = sig_table.cell(r_idx, c_idx)
            cell.width = Inches(2.9)
            set_cell_margins(cell, top=200, bottom=160, left=60, right=60)
            p = cell.paragraphs[0]
            p.alignment = align
            p.paragraph_format.line_spacing = 1.3
            r = p.add_run(text)
            r.bold = True
            r.font.name = 'Times New Roman'
            r.font.size = Pt(11)

    doc.add_page_break()

    # =========================================================
    # 3. ACKNOWLEDGEMENT PAGE (Specimen Format from sample doc)
    # =========================================================
    p_ack_t = doc.add_paragraph()
    p_ack_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_ack_t.paragraph_format.space_before = Pt(8)
    p_ack_t.paragraph_format.space_after = Pt(16)
    r_at = p_ack_t.add_run("ACKNOWLEDGEMENT")
    r_at.bold = True
    r_at.font.name = 'Times New Roman'
    r_at.font.size = Pt(14)

    ack_paras = [
        "I take this opportunity to express my profound gratitude to the faculty and authorities of NIMS University Rajasthan, Jaipur, whose constant encouragement made it possible to undertake and successfully complete this project on Real-Time ATM Card Fraud Detection & Behavioral Risk Analysis System (CardShield).",
        "I express my deepest gratitude and sincere thanks to my project guide and faculty mentor, Prof. Ms. Mohini Fulzele (Assistant Professor), for her invaluable technical support, constructive guidance, encouragement, and consistent help throughout the design, development, and evaluation stages of this project. She has been a constant source of inspiration and guidance to me.",
        "I am also deeply grateful to the Department of Computer Applications and the Cognitive Science – Project Based Learning Lab at Marik Institute of Computing, Artificial Intelligence, Robotics & Cybernetics for providing the computational facilities, laboratory resources, and academic environment necessary to execute this work.",
        "Finally, I express my sincere thanks to my family, friends, and peers who provided encouragement, feedback, and support throughout the duration of the BCA course and the completion of this project report."
    ]

    for txt in ack_paras:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.first_line_indent = Inches(0.5)
        p.paragraph_format.space_after = Pt(8)
        r = p.add_run(txt)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)

    p_sig = doc.add_paragraph()
    p_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sig.paragraph_format.space_before = Pt(24)
    p_sig.paragraph_format.line_spacing = 1.3
    r_s = p_sig.add_run("Mr. Suryapal Singh\n(Enrollment No. 2024COMPSC0029)\nStudent ID: 146476\nBCA – 5th Semester")
    r_s.bold = True
    r_s.font.name = 'Times New Roman'
    r_s.font.size = Pt(11)

    doc.add_page_break()

    # =========================================================
    # 4. INDEX (Table of Contents - Specimen Table Format)
    # =========================================================
    p_idx_t = doc.add_paragraph()
    p_idx_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_idx_t.paragraph_format.space_before = Pt(8)
    p_idx_t.paragraph_format.space_after = Pt(14)
    r_it = p_idx_t.add_run("INDEX")
    r_it.bold = True
    r_it.font.name = 'Times New Roman'
    r_it.font.size = Pt(14)

    index_table = doc.add_table(rows=1, cols=3)
    index_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    index_table.autofit = False
    set_table_borders(index_table, color="7F8C8D", sz="4")

    hdr_cells = index_table.rows[0].cells
    hdr_cells[0].width = Inches(1.0)
    hdr_cells[1].width = Inches(4.2)
    hdr_cells[2].width = Inches(1.0)

    hdr_titles = ["Sr. No.", "Title", "Page No."]
    for idx, c in enumerate(hdr_cells):
        set_cell_background(c, "EAECEE")
        set_cell_margins(c, top=120, bottom=120, left=100, right=100)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if idx != 1 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(hdr_titles[idx])
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    index_entries = [
        ("", "Abstract", "v"),
        ("", "Preface", "vi"),
        ("", "List of Figures", "vii"),
        ("", "List of Tables", "viii"),
        ("", "List of Abbreviations", "ix"),
        ("1", "Introduction", "1"),
        ("  1.1", "Motivation & Historical Evolution of ATM Banking Fraud", "1"),
        ("  1.2", "ATM Architecture & Vulnerability Landscape", "2"),
        ("  1.3", "Threat Vector Taxonomy (Skimming, Brute-Force, Velocity)", "3"),
        ("  1.4", "Problem Statement & The Accuracy Paradox Challenge", "4"),
        ("  1.5", "Project Objectives & Success Criteria", "5"),
        ("  1.6", "Work Plan Schedule & Timeline", "6"),
        ("  1.7", "Project Submission Details & Deliverables", "7"),
        ("  1.8", "Scope and Limitations of the Study", "8"),
        ("  1.9", "Organization of the Report", "8"),
        ("2", "Literature Survey", "9"),
        ("  2.1", "Literature Review & Historical Evolution of Fraud Detection", "9"),
        ("  2.2", "Survey of Supervised & Unsupervised Machine Learning", "11"),
        ("  2.3", "Existing Rule-Based Engines and Their Critical Vulnerabilities", "13"),
        ("  2.4", "The Accuracy Paradox: Formal Mathematical Formulation", "15"),
        ("  2.5", "Comparative Matrix of Contemporary Approaches", "17"),
        ("3", "Proposed System", "18"),
        ("  3.1", "Proposed System Overview & Defense-in-Depth Topology", "18"),
        ("  3.2", "Multi-Tier System Architecture (UI, Flask, AI Engine)", "20"),
        ("  3.3", "System Working Description & Execution Pipeline", "22"),
        ("  3.4", "Flowchart / Data Flow Diagrams (DFD Level 0 & Level 1)", "24"),
        ("  3.5", "7-Dimensional Behavioral Risk Engine Formulation", "26"),
        ("  3.6", "Decision Risk Levels & Automated Operational Responses", "28"),
        ("4", "Methodology", "30"),
        ("  4.1", "Implementation Details & Agile Lifecycle", "30"),
        ("  4.2", "Synthetic Dataset Architecture (100,000 Bank Records)", "31"),
        ("  4.3", "Feature Engineering & Label Encoding Pipelines", "33"),
        ("  4.4", "Cost-Sensitive Balanced Random Forest Formulation", "35"),
        ("  4.5", "Hyperparameter Optimization & Cross-Validation Protocol", "37"),
        ("  4.6", "Description of Software Used", "38"),
        ("  4.7", "Description of Hardware Used & Operational Environment", "40"),
        ("  4.8", "Security Architecture, TLS 1.3 & PCI-DSS Compliance", "41"),
        ("5", "Results and Discussion", "43"),
        ("  5.1", "Sample Output & Real-World Transaction Simulations", "43"),
        ("  5.2", "Results & Comprehensive Model Performance Metrics", "46"),
        ("  5.3", "Live Anomaly Stream & Instant Alert Notification", "48"),
        ("  5.4", "Forensic Audit Trail & Threat Vector Inspection", "50"),
        ("  5.5", "ROC-AUC Analysis & Discrimination Capability", "52"),
        ("  5.6", "Comparison with Existing Systems & Accuracy Paradox Resolution", "54"),
        ("  5.7", "Latency Profiling & Verification Response Time (< 85ms)", "55"),
        ("  5.8", "Real-World Applications in Banking & ATM Networks", "56"),
        ("6", "Conclusion and Future Scope", "58"),
        ("  6.1", "Conclusion & Summary of Engineering Contributions", "58"),
        ("  6.2", "Future Scope & Emerging Technologies", "59"),
        ("7", "References", "61"),
        ("8", "Appendix", "64"),
        ("  8.1", "Appendix A: Complete Flask & Machine Learning Source Code", "64"),
        ("  8.2", "Appendix B: RESTful API Specifications & Data Payloads", "68"),
    ]

    for sr, title, pg in index_entries:
        row = index_table.add_row()
        c0, c1, c2 = row.cells
        c0.width = Inches(1.0)
        c1.width = Inches(4.2)
        c2.width = Inches(1.0)
        
        is_main = sr in ["1", "2", "3", "4", "5", "6", "7", "8"] or sr == ""
        if is_main:
            set_cell_background(c0, "F8F9F9")
            set_cell_background(c1, "F8F9F9")
            set_cell_background(c2, "F8F9F9")

        for c, text, align in [(c0, sr, WD_ALIGN_PARAGRAPH.CENTER), (c1, title, WD_ALIGN_PARAGRAPH.LEFT), (c2, pg, WD_ALIGN_PARAGRAPH.CENTER)]:
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            p = c.paragraphs[0]
            p.alignment = align
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.bold = is_main
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)

    doc.add_page_break()

    # =========================================================
    # 5. ABSTRACT PAGE (Specimen Format from sample doc)
    # =========================================================
    p_abs_t = doc.add_paragraph()
    p_abs_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_abs_t.paragraph_format.space_before = Pt(8)
    p_abs_t.paragraph_format.space_after = Pt(14)
    r_abst = p_abs_t.add_run("ABSTRACT")
    r_abst.bold = True
    r_abst.font.name = 'Times New Roman'
    r_abst.font.size = Pt(14)

    abs_p1 = (
        "The exponential expansion of digital banking and automated teller machine (ATM) card infrastructure has revolutionized modern consumer "
        "convenience while simultaneously precipitating unprecedented financial fraud attacks. Contemporary banking security architectures "
        "routinely struggle to defend against sophisticated attack vectors, including physical card skimming, PIN credential brute-forcing, "
        "unauthorized velocity spikes, and geographically impossible transacting. Conventional anti-fraud defenses have traditionally relied upon "
        "static rule engines that operate under rigid parametric thresholds. These legacy paradigms suffer from severe latency, generate excessive "
        "false alarm rates that disrupt legitimate banking consumers, and remain fundamentally incapable of detecting novel zero-day behavioral anomalies."
    )
    abs_p2 = (
        "A critical foundational dilemma in machine-learning-driven financial security is the phenomenon known as the 'Accuracy Paradox'. In real-world "
        "banking datasets, approximately 99.5% of transactions are legitimate and only 0.5% are fraudulent. When standard machine learning classification models "
        "are trained on such imbalanced data without cost-sensitive compensation, they routinely converge on predicting the majority non-fraudulent class exclusively. "
        "Such naive models achieve deceptive nominal accuracy scores exceeding 99.5% while failing to detect a single true fraudulent transaction, rendering them "
        "operationally catastrophic in production banking environments."
    )
    abs_p3 = (
        "To resolve these systemic vulnerabilities, this project presents CardShield: an enterprise-grade, real-time web-based ATM card fraud detection and "
        "multi-factor behavioral risk analysis platform. CardShield employs a cost-sensitive Balanced Random Forest classifier ensembled with an intelligent "
        "7-dimensional dynamic behavioral heuristic engine. The AI model was trained on 100,000 real-world-modeled bank transaction records, successfully catching "
        "78.4% of rare fraud attempts (Recall) with an outstanding 86.5% overall ROC-AUC quality score, while executing inference in under 85 milliseconds. "
        "The behavioral engine evaluates seven critical factors: Card Status (Blocked/Expired), Transaction Amount (vs. baseline average), Time of Day (Midnight to 4 AM), "
        "Location (Domestic vs. International), Merchant Category, 24-Hour Velocity Frequency, and Credit Limit Utilization. Transactions are categorized into "
        "three actionable risk levels: Low Risk (0–39, Approve), Medium Risk (40–69, Send Step-up OTP), and High Risk / Fraud (70–100, Decline & Block Card). "
        "The platform is delivered through an interactive cyber defense operations console featuring an animated speedometer gauge, real-time telemetry bars, "
        "and simulated testing profiles."
    )

    for txt in [abs_p1, abs_p2, abs_p3]:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.first_line_indent = Inches(0.5)
        p.paragraph_format.space_after = Pt(8)
        r = p.add_run(txt)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)

    p_terms = doc.add_paragraph()
    p_terms.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_terms.paragraph_format.line_spacing = 1.5
    p_terms.paragraph_format.first_line_indent = Inches(0.5)
    p_terms.paragraph_format.space_before = Pt(8)
    p_terms.paragraph_format.space_after = Pt(0)
    r_term_lbl = p_terms.add_run("Index Terms — ")
    r_term_lbl.bold = True
    r_term_lbl.font.name = 'Times New Roman'
    r_term_lbl.font.size = Pt(12)
    r_term_val = p_terms.add_run("ATM Fraud Detection, Behavioral Risk Scoring, Machine Learning, Random Forest, Flask Web Architecture, Real-Time Cybersecurity, Transaction Velocity, Accuracy Paradox.")
    r_term_val.italic = True
    r_term_val.font.name = 'Times New Roman'
    r_term_val.font.size = Pt(12)

    doc.add_page_break()

    # =========================================================
    # 6. PREFACE PAGE (Specimen Format from sample doc)
    # =========================================================
    p_pref_t = doc.add_paragraph()
    p_pref_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_pref_t.paragraph_format.space_before = Pt(8)
    p_pref_t.paragraph_format.space_after = Pt(14)
    r_pt = p_pref_t.add_run("PREFACE")
    r_pt.bold = True
    r_pt.font.name = 'Times New Roman'
    r_pt.font.size = Pt(14)

    pref_paras = [
        "In the contemporary global economy, financial card payment systems and Automated Teller Machine (ATM) networks serve as the fundamental arteries of daily commerce. Hundreds of millions of citizens rely on debit and credit cards for retail procurement, essential cash withdrawals, and electronic bill settlements. However, as payment systems have expanded in velocity and interconnectedness, financial crime syndicates have evolved from rudimentary physical theft into highly sophisticated, automated cyber threats.",
        "Traditional banking security postures have historically relied upon static rule engines that operate under fixed thresholds, such as flagging any transaction exceeding a preconfigured dollar amount or rejecting transactions after three incorrect PIN entries. While these rules provide basic baseline protection, they are completely inadequate against modern fraud vectors. Fraud syndicates utilize sophisticated skimming devices at ATM vestibules, dark-web credential databases, automated velocity bots, and synthetic identity fraud. Furthermore, legacy rule engines suffer from an excessive false-positive rate, blocking innocent customers at the point of sale and inflicting immense operational overhead on banking customer support desks.",
        "The advent of artificial intelligence and machine learning offers a powerful paradigm shift. Rather than relying on rigid, human-authored rules, machine learning models can learn complex non-linear patterns across multidimensional transaction features. Nevertheless, deploying machine learning in production financial institutions introduces acute technical challenges: extreme class imbalance, the Accuracy Paradox, millisecond latency constraints, and the vital necessity of human interpretability for regulatory compliance.",
        "This project report, developed under the 5th-Semester Problem-Based Learning (PBL) curriculum of the Bachelor of Computer Applications (BCA) program at Cognitive Science - Project Based Learning Lab, Marik Institute of Computing, Artificial Intelligence, Robotics & Cybernetics, NIMS University Rajasthan, Jaipur, documents the engineering design, mathematical formulation, and full-stack software implementation of CardShield. CardShield bridges the gap between theoretical machine learning research and real-world banking operations by uniting a cost-sensitive Balanced Random Forest classifier with an intelligent 7-factor behavioral risk engine.",
        "It is our sincere hope that the methodologies, empirical benchmarks, and system architectures documented in this report will offer practical insights to students, researchers, and financial software engineers striving to create a safer, fraud-resilient digital financial ecosystem."
    ]

    for txt in pref_paras:
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.line_spacing = 1.5
        p.paragraph_format.first_line_indent = Inches(0.5)
        p.paragraph_format.space_after = Pt(8)
        r = p.add_run(txt)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)

    doc.add_page_break()

    # =========================================================
    # 7. LIST OF FIGURES (Specimen Table Format)
    # =========================================================
    p_lof_t = doc.add_paragraph()
    p_lof_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lof_t.paragraph_format.space_before = Pt(8)
    p_lof_t.paragraph_format.space_after = Pt(14)
    r_loft = p_lof_t.add_run("LIST OF FIGURES")
    r_loft.bold = True
    r_loft.font.name = 'Times New Roman'
    r_loft.font.size = Pt(14)

    fig_table = doc.add_table(rows=1, cols=3)
    fig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    fig_table.autofit = False
    set_table_borders(fig_table, color="7F8C8D", sz="4")

    fhdr_cells = fig_table.rows[0].cells
    fhdr_cells[0].width = Inches(1.0)
    fhdr_cells[1].width = Inches(4.2)
    fhdr_cells[2].width = Inches(1.0)

    for idx, c in enumerate(fhdr_cells):
        set_cell_background(c, "EAECEE")
        set_cell_margins(c, top=120, bottom=120, left=100, right=100)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if idx != 1 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(hdr_titles[idx])
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    figure_entries = [
        ("3.1", "CardShield Multi-Tier Architecture & Data Exchange Pipeline", "20"),
        ("3.2", "CardShield Data Flow Diagram (DFD Level 1 Context Architecture)", "24"),
        ("3.3", "CardShield 7-Dimensional Behavioral Risk Engine Weights (Sum = 100%)", "27"),
        ("5.1", "CardShield Executive Cyber Defense Dashboard (Live UI)", "44"),
        ("5.2", "Real-Time Transaction Stream & Automated Anomaly Feed", "45"),
        ("5.3", "Real-Time Behavioral Threat Diagnostics & Risk Gauge", "49"),
        ("5.4", "Instant High-Risk Incident Alert & Account Lockdown Notification", "50"),
        ("5.5", "Forensic Audit Timeline & Suspicious Vector Inspection", "51"),
        ("5.6", "Receiver Operating Characteristic (ROC-AUC) Comparative Analysis", "53"),
        ("5.7", "Performance Benchmark: Raw Accuracy vs CardShield Fraud Detection", "55"),
    ]

    for sr, caption, pg in figure_entries:
        row = fig_table.add_row()
        c0, c1, c2 = row.cells
        c0.width = Inches(1.0)
        c1.width = Inches(4.2)
        c2.width = Inches(1.0)
        for c, text, align in [(c0, sr, WD_ALIGN_PARAGRAPH.CENTER), (c1, caption, WD_ALIGN_PARAGRAPH.LEFT), (c2, pg, WD_ALIGN_PARAGRAPH.CENTER)]:
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            p = c.paragraphs[0]
            p.alignment = align
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)

    doc.add_page_break()

    # =========================================================
    # 8. LIST OF TABLES (Specimen Table Format)
    # =========================================================
    p_lot_t = doc.add_paragraph()
    p_lot_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_lot_t.paragraph_format.space_before = Pt(8)
    p_lot_t.paragraph_format.space_after = Pt(14)
    r_lott = p_lot_t.add_run("LIST OF TABLES")
    r_lott.bold = True
    r_lott.font.name = 'Times New Roman'
    r_lott.font.size = Pt(14)

    tab_table = doc.add_table(rows=1, cols=3)
    tab_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    tab_table.autofit = False
    set_table_borders(tab_table, color="7F8C8D", sz="4")

    thdr_cells = tab_table.rows[0].cells
    thdr_cells[0].width = Inches(1.0)
    thdr_cells[1].width = Inches(4.2)
    thdr_cells[2].width = Inches(1.0)

    for idx, c in enumerate(thdr_cells):
        set_cell_background(c, "EAECEE")
        set_cell_margins(c, top=120, bottom=120, left=100, right=100)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER if idx != 1 else WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(["Sr. No.", "Table Caption", "Page No."][idx])
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    table_entries = [
        ("1.1", "Work Plan Schedule & Milestone Execution Timeline", "6"),
        ("1.2", "Project Deliverables & Academic Submission Specifications", "7"),
        ("2.1", "Comparative Analysis of Contemporary ATM Fraud Detection Systems", "17"),
        ("3.1", "CardShield 7-Dimensional Behavioral Risk Weight Matrix", "27"),
        ("3.2", "Decision Risk Levels & Automated Operational Responses", "29"),
        ("4.1", "Software Development Environment & Tech Stack Specifications", "39"),
        ("4.2", "Hardware & System Operational Requirements", "41"),
        ("5.1", "Model Performance Evaluation & Fraud Detection Metrics", "47"),
    ]

    for sr, caption, pg in table_entries:
        row = tab_table.add_row()
        c0, c1, c2 = row.cells
        c0.width = Inches(1.0)
        c1.width = Inches(4.2)
        c2.width = Inches(1.0)
        for c, text, align in [(c0, sr, WD_ALIGN_PARAGRAPH.CENTER), (c1, caption, WD_ALIGN_PARAGRAPH.LEFT), (c2, pg, WD_ALIGN_PARAGRAPH.CENTER)]:
            set_cell_margins(c, top=60, bottom=60, left=80, right=80)
            p = c.paragraphs[0]
            p.alignment = align
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)

    doc.add_page_break()

    # =========================================================
    # 9. LIST OF ABBREVIATIONS (Specimen Table Format)
    # =========================================================
    p_loa_t = doc.add_paragraph()
    p_loa_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_loa_t.paragraph_format.space_before = Pt(8)
    p_loa_t.paragraph_format.space_after = Pt(14)
    r_loat = p_loa_t.add_run("LIST OF ABBREVIATIONS")
    r_loat.bold = True
    r_loat.font.name = 'Times New Roman'
    r_loat.font.size = Pt(14)

    abbr_table = doc.add_table(rows=1, cols=2)
    abbr_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    abbr_table.autofit = False
    set_table_borders(abbr_table, color="7F8C8D", sz="4")

    ahdr_cells = abbr_table.rows[0].cells
    ahdr_cells[0].width = Inches(2.0)
    ahdr_cells[1].width = Inches(4.2)

    for idx, c in enumerate(ahdr_cells):
        set_cell_background(c, "EAECEE")
        set_cell_margins(c, top=120, bottom=120, left=100, right=100)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(["Abbreviation", "Description / Full Form"][idx])
        r.bold = True
        r.font.name = 'Times New Roman'
        r.font.size = Pt(11)

    abbreviations = [
        ("ATM", "Automated Teller Machine"),
        ("BCA", "Bachelor of Computer Applications"),
        ("PBL", "Problem Based Learning"),
        ("API", "Application Programming Interface"),
        ("ROC-AUC", "Receiver Operating Characteristic - Area Under Curve"),
        ("ML", "Machine Learning"),
        ("RF", "Random Forest Classifier"),
        ("PIN", "Personal Identification Number"),
        ("CVV", "Card Verification Value"),
        ("OTP", "One-Time Password"),
        ("MFA", "Multi-Factor Authentication"),
        ("JSON", "JavaScript Object Notation"),
        ("REST", "Representational State Transfer"),
        ("HTML", "HyperText Markup Language"),
        ("CSS", "Cascading Style Sheets"),
        ("JS", "JavaScript (ECMAScript 6+)"),
        ("DFD", "Data Flow Diagram"),
        ("ERD", "Entity Relationship Diagram"),
        ("OS", "Operating System"),
        ("RAM", "Random Access Memory"),
        ("CPU", "Central Processing Unit"),
        ("CSV", "Comma-Separated Values"),
        ("SDK", "Software Development Kit"),
        ("SMOTE", "Synthetic Minority Over-sampling Technique"),
        ("TPR", "True Positive Rate (Recall)"),
        ("FPR", "False Positive Rate"),
        ("UI", "User Interface"),
        ("HTTP", "HyperText Transfer Protocol"),
        ("CORS", "Cross-Origin Resource Sharing"),
        ("PCI-DSS", "Payment Card Industry Data Security Standard"),
        ("TLS", "Transport Layer Security"),
    ]

    for abbr, full_form in abbreviations:
        row = abbr_table.add_row()
        c0, c1 = row.cells
        c0.width = Inches(2.0)
        c1.width = Inches(4.2)
        for c, text in [(c0, abbr), (c1, full_form)]:
            set_cell_margins(c, top=50, bottom=50, left=80, right=80)
            p = c.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.line_spacing = 1.15
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            r = p.add_run(text)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(10)
            if c == c0:
                r.bold = True

    doc.add_page_break()
    print("Updated front matter generated successfully.")
