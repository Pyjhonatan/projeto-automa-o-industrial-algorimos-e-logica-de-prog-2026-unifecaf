from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def gerar(stats):

    c = canvas.Canvas("relatorio_producao.pdf",pagesize=letter)

    y = 750

    c.drawString(100,y,"RELATORIO PRODUCAO INDUSTRIAL")

    y -= 40
    c.drawString(100,y,f"Aprovadas: {stats['aprovadas']}")

    y -= 20
    c.drawString(100,y,f"Reprovadas: {stats['reprovadas']}")

    y -= 20
    c.drawString(100,y,f"Caixas usadas: {stats['caixas']}")

    y -= 40
    c.drawString(100,y,"Motivos de reprovacao")

    y -= 20

    for m,q in stats["motivos"].items():
        c.drawString(120,y,f"{m}: {q}")
        y -= 20

    c.save()