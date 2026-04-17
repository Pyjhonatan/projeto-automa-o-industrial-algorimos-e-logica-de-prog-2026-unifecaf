import tkinter as tk
from tkinter import messagebox

from sistema_producao import SistemaProducao,Peca
from database import conectar,salvar
from export_excel import exportar
from relatorio_pdf import gerar
from dashboard import mostrar

sistema = SistemaProducao()
conn = conectar()


def registrar():

    try:

        id = entry_id.get()
        peso = float(entry_peso.get())
        cor = entry_cor.get()
        comp = float(entry_comp.get())

        peca = Peca(id,peso,cor,comp)

        aprovado,motivo = sistema.processar(peca)

        status = "Aprovada" if aprovado else "Reprovada"

        salvar(conn,peca,status,motivo)

        messagebox.showinfo("Resultado",status + " | " + motivo)

    except:
        messagebox.showerror("Erro","Dados invalidos")


def relatorio():

    stats = sistema.estatisticas()

    gerar(stats)
    exportar()

    messagebox.showinfo("Relatorio","PDF e Excel gerados")


def dashboard():

    stats = sistema.estatisticas()
    mostrar(stats)


janela = tk.Tk()
janela.title("Controle de Producao Industrial")


tk.Label(janela,text="ID").grid(row=0,column=0)
entry_id = tk.Entry(janela)
entry_id.grid(row=0,column=1)


tk.Label(janela,text="Peso").grid(row=1,column=0)
entry_peso = tk.Entry(janela)
entry_peso.grid(row=1,column=1)


tk.Label(janela,text="Cor").grid(row=2,column=0)
entry_cor = tk.Entry(janela)
entry_cor.grid(row=2,column=1)


tk.Label(janela,text="Comprimento").grid(row=3,column=0)
entry_comp = tk.Entry(janela)
entry_comp.grid(row=3,column=1)


tk.Button(janela,text="Registrar Peca",command=registrar).grid(row=4,columnspan=2)

tk.Button(janela,text="Gerar Relatorios",command=relatorio).grid(row=5,columnspan=2)

tk.Button(janela,text="Dashboard",command=dashboard).grid(row=6,columnspan=2)


janela.mainloop()