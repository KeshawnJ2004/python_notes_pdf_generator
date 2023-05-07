# Import modules
from fpdf import FPDF
import pandas as pd

# Create pandas dataframe.
df = pd.read_csv('topics2.csv')

# Create PDF instance.
pdf = FPDF(orientation='P', unit='mm', format='A4')

# Pages should not be broken automatically.
pdf.set_auto_page_break(auto=False, margin=0)

# Iterate over each row in dataframe.
# Create x amount of pages, let x = row['Pages']
# x is an integer. row is in df.iterrows()
for index, row in df.iterrowss():
    pdf.add_page()

    # Set the header
    pdf.set_font(family='Times', style='B', size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1, border=1)
    pdf.line(10, 21, 200, 21)

    # Set the page footer.
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=10)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    # Add more pages for each topic.
    for i in range(row['Pages'] - 1):
        pdf.add_page()

        # Set the page footer for additional pages.
        pdf.ln(277)
        pdf.set_font(family='Times', style='I', size=10)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

# Output PDF file.
pdf.output('output.pdf')
