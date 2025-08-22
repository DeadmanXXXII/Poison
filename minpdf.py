from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, "Hello if this is uploaded you have a critical vulnerability.\nContact BugCrowd and ask for DeadmanXXXII P1 dangerous file inclusion report.")
pdf.output("container.pdf")
