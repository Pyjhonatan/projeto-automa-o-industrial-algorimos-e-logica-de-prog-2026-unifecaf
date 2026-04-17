import sqlite3

def conectar():

    conn = sqlite3.connect("producao.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pecas(
        id TEXT,
        peso REAL,
        cor TEXT,
        comprimento REAL,
        status TEXT,
        motivo TEXT
    )
    """)

    conn.commit()
    return conn


def salvar(conn, peca, status, motivo):

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO pecas VALUES (?,?,?,?,?,?)",
        (peca.id,peca.peso,peca.cor,peca.comprimento,status,motivo)
    )

    conn.commit()