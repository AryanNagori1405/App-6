from fpdf import FPDF
import glob
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("text files/*.txt")

# Create a PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Iterate over each of the text file
for filepath in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get the filename without the extension
    file_path = Path(filepath).stem
    # Convert it to title case(e.g. Cat)
    filename = file_path.title()

    # Add the name of the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename, ln=1)
    # Add a line below the name
    pdf.line(10, 18, 200, 18)

    # Get the content of the text file
    with open(filepath) as file:
        content = file.read()
    # Add the text file content to PDF
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=10, txt=content)

# Produce the PDF
pdf.output("output.pdf")
