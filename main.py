from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("text files/*.txt")

pdf = FPDF(orientation="P", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()

    file_path = Path(filepath).stem
    filename = file_path.title()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=filename, ln=1)
    pdf.line(10, 20, 200, 20)

    with open(filename) as file:
        file_info = file.read()

    pdf.set_font(family="Times", size=12)
    pdf.cell(w=15, h=15, txt=file_info, ln=True)

pdf.output("output.pdf")
