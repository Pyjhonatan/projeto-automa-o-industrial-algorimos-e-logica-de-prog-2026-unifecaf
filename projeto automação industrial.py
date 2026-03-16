class Peca:
    def __init__(self, id, peso, cor, comprimento):
        self.id = id
        self.peso = peso
        self.cor = cor.lower()
        self.comprimento = comprimento


class SistemaProducao:

    CAPACIDADE_CAIXA = 10

    def __init__(self):
        self.caixas = [[]]
        self.reprovadas = []
        self.aprovadas = 0
        self.motivos_reprovacao = {
            "peso": 0,
            "cor": 0,
            "comprimento": 0
        }

    def verificar_qualidade(self, peca):
        motivos = []

        if not (95 <= peca.peso <= 105):
            motivos.append("peso")

        if peca.cor not in ["azul", "verde"]:
            motivos.append("cor")

        if not (10 <= peca.comprimento <= 20):
            motivos.append("comprimento")

        return motivos

    def armazenar_peca(self, peca):
        caixa_atual = self.caixas[-1]

        if len(caixa_atual) >= self.CAPACIDADE_CAIXA:
            print("📦 Caixa cheia. Fechando caixa e abrindo nova.")
            self.caixas.append([])
            caixa_atual = self.caixas[-1]

        caixa_atual.append(peca)

    def processar_peca(self, peca):

        motivos = self.verificar_qualidade(peca)

        if len(motivos) == 0:
            self.aprovadas += 1
            self.armazenar_peca(peca)
            print(f"Peça {peca.id} APROVADA")
        else:
            self.reprovadas.append((peca, motivos))

            for m in motivos:
                self.motivos_reprovacao[m] += 1

            print(f"Peça {peca.id} REPROVADA -> Motivo: {', '.join(motivos)}")

    def gerar_relatorio(self):

        total_reprovadas = len(self.reprovadas)

        caixas_utilizadas = len(self.caixas)

        print("\n===== RELATÓRIO DE PRODUÇÃO =====")

        print(f"Total de peças aprovadas: {self.aprovadas}")

        print(f"Total de peças reprovadas: {total_reprovadas}")

        print("\nMotivos de reprovação:")

        for motivo, qtd in self.motivos_reprovacao.items():
            print(f"{motivo}: {qtd}")

        print(f"\nQuantidade de caixas utilizadas: {caixas_utilizadas}")


def main():

    sistema = SistemaProducao()

    while True:

        print("\nDigite os dados da peça")

        id = input("ID da peça: ")
        peso = float(input("Peso (g): "))
        cor = input("Cor: ")
        comprimento = float(input("Comprimento (cm): "))

        peca = Peca(id, peso, cor, comprimento)

        sistema.processar_peca(peca)

        continuar = input("Deseja inserir outra peça? (s/n): ")

        if continuar.lower() != "s":
            break

    sistema.gerar_relatorio()


if __name__ == "__main__":
    main()