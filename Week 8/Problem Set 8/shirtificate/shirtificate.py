from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, student="Someone"):
        super().__init__()
        self.student = student

    def header(self):
        self.image("shirtificate.png", 5, 75, 200)
        self.set_font("helvetica", style="B", size=50)
        self.cell(80)
        self.cell(30, 50, "CS50 Shirtificate", border=0, align="C")
        self.set_text_color(255,255,255)
        self.set_font("helvetica", style="B", size=25)
        self.cell(-30, 250, f"{self.student} took CS50", border=0, align="C")

pdf = PDF(input("Name: "))
pdf.output("shirtificate.pdf")
