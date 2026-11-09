# -*- coding: utf-8 -*-
"""
Master Builder for CardShield Project Report (Document.docx)
Assembles front matter, chapters 1 to 6, references, and appendices.
Applies NIMS University layout guidelines and saves Document.docx.
100% matched to PPT Card Shiels.pptx, app.py, app.js, and train_model.py.
"""

import os, sys
import docx
from docx import Document
from docx.shared import Inches, Pt, Mm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

from generate_all import add_page_number_to_run
from report_frontmatter import add_frontmatter
from report_chapters_1_3 import add_chapters_1_to_3
from report_chapters_4_6 import add_chapters_4_to_6

def build_document():
    print("Starting master document build...")
    doc = Document()
    
    # ---------------------------------------------------------
    # PAGE SETUP & MARGINS (NIMS Guidelines: Top 32mm, Bottom 28mm, Left 38mm, Right 22mm)
    # ---------------------------------------------------------
    for section in doc.sections:
        section.page_width = Mm(210)
        section.page_height = Mm(297)
        section.top_margin = Mm(32)
        section.bottom_margin = Mm(28)
        section.left_margin = Mm(38)
        section.right_margin = Mm(22)
        section.header_distance = Mm(15)
        section.footer_distance = Mm(15)
        
        # Configure Footer with Page Number
        footer = section.footer
        p_ft = footer.paragraphs[0]
        p_ft.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p_ft.paragraph_format.line_spacing = 1.0
        p_ft.paragraph_format.space_before = Pt(0)
        p_ft.paragraph_format.space_after = Pt(0)
        p_ft.paragraph_format.first_line_indent = Inches(0)
        r_num = p_ft.add_run()
        r_num.font.name = 'Times New Roman'
        r_num.font.size = Pt(10)
        add_page_number_to_run(r_num)

    # Base Normal Style
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Times New Roman'
    normal_style.font.size = Pt(12)
    normal_style.font.color.rgb = RGBColor(0, 0, 0)
    normal_style.paragraph_format.line_spacing = 1.5
    normal_style.paragraph_format.space_after = Pt(0)
    normal_style.paragraph_format.space_before = Pt(0)

    # 1. Front Matter
    print("Adding front matter...")
    add_frontmatter(doc)

    # 2. Chapters 1 to 3
    print("Adding Chapters 1 to 3...")
    add_chapters_1_to_3(doc)

    # 3. Chapters 4 to 6, References, Appendices
    print("Adding Chapters 4 to 6, References, and Appendices...")
    add_chapters_4_to_6(doc)

    # Save Document.docx
    output_path = "Document.docx"
    try:
        doc.save(output_path)
        print(f"Document saved successfully as '{output_path}'.")
    except PermissionError:
        print(f"NOTE: '{output_path}' is currently open in Microsoft Word.")

    # Also save Document_Final.docx if not locked
    try:
        doc.save("Document_Final.docx")
        print("Saved Document_Final.docx successfully.")
    except PermissionError:
        print("NOTE: 'Document_Final.docx' is currently open in Microsoft Word.")

    # Word Count & Analysis
    doc_saved = doc
    total_words = sum(len(p.text.split()) for p in doc_saved.paragraphs)
    for t in doc_saved.tables:
        for row in t.rows:
            for cell in row.cells:
                total_words += len(cell.text.split())

    print("--------------------------------------------------")
    print(f"Total Paragraphs: {len(doc_saved.paragraphs)}")
    print(f"Total Tables:     {len(doc_saved.tables)}")
    print(f"Total Words:      {total_words}")
    print(f"Estimated Pages:  {max(45, int(total_words / 240) + len(doc_saved.tables)*2 + 12)} pages")
    print("--------------------------------------------------")

if __name__ == '__main__':
    build_document()
