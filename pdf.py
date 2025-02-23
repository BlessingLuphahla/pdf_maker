from fpdf import FPDF

"""
This script reads text content from a file named 'pdf.txt', generates a PDF document using the FPDF library, and saves the PDF as 'output.pdf'.

Modules:
    fpdf: A library for generating PDF documents in Python.

Usage:
    Run this script to convert the text content from 'pdf.txt' into a PDF file.

Functions:
    None

Procedure:
    1. Import the FPDF class from the fpdf module.
    2. Read the text content from 'pdf.txt'.
    3. Initialize a new PDF document.
    4. Set up the page layout with automatic page breaks.
    5. Add a font (Arial Unicode) to the PDF.
    6. Add the text content to the PDF using multi-cell formatting.
    7. Save the generated PDF as 'output.pdf'.
"""


# Define the text content
with open("pdf.txt", "r") as file:
  text_content = file.read()

  # Initialize PDF
  pdf = FPDF()
  pdf.set_auto_page_break(auto=True, margin=15)
  pdf.add_page()

  # Set the font to Arial Unicode
  pdf.add_font('Arial', '', 'arial.ttf', uni=True)
  pdf.set_font('Arial', '', 12)

  # Add text to PDF
  pdf.multi_cell(0, 8, text_content)

  # Save the PDF
  pdf.output("output.pdf")
