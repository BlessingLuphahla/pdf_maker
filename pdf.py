from fpdf import FPDF

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
  pdf.output("Payday_Platform_Design_Plan.pdf")

  print("output.pdf")
