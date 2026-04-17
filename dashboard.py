import matplotlib.pyplot as plt

def mostrar(stats):

    labels = list(stats["motivos"].keys())
    valores = list(stats["motivos"].values())

    plt.bar(labels,valores)

    plt.title("Motivos de Reprovacao")
    plt.xlabel("Tipo")
    plt.ylabel("Quantidade")

    plt.show()