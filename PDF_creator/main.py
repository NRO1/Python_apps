from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
frame = pd.read_csv("topics.csv")

for idx, row in frame.iterrows():
    pdf.add_page()
    pdf.set_font(family="arial", style="", size=24)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.set_draw_color(120, 120, 120)
    pdf.line(10, 21, 200, 21 )
    
    for x in (range(row["Pages"] -1 )):
        pdf.add_page()

pdf.output("output.pdf")