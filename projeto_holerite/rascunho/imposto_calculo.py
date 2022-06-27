class Imposto:
    
    def __init__(self, lista_aliquota: list, lista_remuneracao: list[tuple(float)], lista_deducao: list):
        self.lista_aliquota: list = lista_aliquota
        self.lista_remuneracao: list = lista_remuneracao
        self.lista_deducao: list = lista_deducao
    
    def contribuicao(self, base_de_calculo):
        
        for i in range(len(self.lista_remuneracao)):
            if  base_de_calculo in list(range(self.lista_remuneracao[i][0], self.lista_remuneracao[i][1])):
                aliquota = self.lista_aliquota[i]
                deducao = self.lista_deducao[i]
                contribuicao = base_de_calculo * aliquota - deducao
            else:
                contribuicao = self.lista_remuneracao[-1][1] * self.lista_aliquota[-1] - self.lista_deducao[-1]
    
        return contribuicao
