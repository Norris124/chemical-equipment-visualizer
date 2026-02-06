from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(summary, path):
    doc = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()
    content = []

    for k, v in summary.items():
        content.append(Paragraph(f"{k}: {v}", styles["Normal"]))

    doc.build(content)
