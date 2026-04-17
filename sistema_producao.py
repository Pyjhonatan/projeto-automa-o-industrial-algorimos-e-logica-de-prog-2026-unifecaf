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
        self.aprovadas = []
        self.reprovadas = []
        self.motivos = {"peso":0,"cor":0,"comprimento":0}

    def verificar(self, peca):

        erros = []

        if not (95 <= peca.peso <= 105):
            erros.append("peso")

        if peca.cor not in ["azul","verde"]:
            erros.append("cor")

        if not (10 <= peca.comprimento <= 20):
            erros.append("comprimento")

        return erros


    def armazenar(self, peca):

        caixa = self.caixas[-1]

        if len(caixa) >= self.CAPACIDADE_CAIXA:
            self.caixas.append([])
            caixa = self.caixas[-1]

        caixa.append(peca)


    def processar(self, peca):

        erros = self.verificar(peca)

        if not erros:

            self.aprovadas.append(peca)
            self.armazenar(peca)

            return True,"Aprovada"

        else:

            for e in erros:
                self.motivos[e]+=1

            self.reprovadas.append((peca,erros))

            return False,", ".join(erros)


    def estatisticas(self):

        return {
            "aprovadas":len(self.aprovadas),
            "reprovadas":len(self.reprovadas),
            "caixas":len(self.caixas),
            "motivos":self.motivos
        }