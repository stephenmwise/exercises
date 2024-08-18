import glob
from fpdf import FPDF
from pathlib import Path

# create a list of text filepaths
filepaths = glob.glob("text_files/*txt")
# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    # Adds a page to the PDF doc for each text file
    pdf.add_page()

    # Add the name to the PDF
    filename = Path(filepath).stem
    newpdfname = filename.title()

    # Add the name to the PDF
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"{newpdfname}", ln=1)

#Produce the PDF
pdf.output("output.pdf")
