import pandas as pd
import sqlite3

def exportar():

    conn = sqlite3.connect("producao.db")

    df = pd.read_sql_query("SELECT * FROM pecas",conn)

    df.to_excel("relatorio_producao.xlsx",index=False)

    conn.close()