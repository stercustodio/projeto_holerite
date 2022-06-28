from src.entities.funcionario import Funcionario

from rascunho.holerite import Holerite


class INSS:

    def __init__(self, funcionario: Funcionario):
        self.__aliquotas_INSS = [0.075, 0.09, 0.12, 0.14]
        self.__intervalo_remuneracao = [
            (0, 1_212),
            (1_212.01, 2_427.35),
            (2_427.36, 3_641.03),
            (3_641.04, 7_087.22)
            ]   
        self.__salario = Holerite.base_calc_INSS()
        
    def calcula_aliquota(self) -> float:
        
        for i in range(4):
            if self.__salario in self.__intervalo_remuneracao[i]:
                aliquota = self.__aliquotas_INSS[i]
                return aliquota
            
        if self.__salario > self.__intervalo_remuneracao[-1][1]:
            aliquota = self.__aliquotas_INSS[-1]
            return aliquota
                
    def parcela_a_deduzir(self):
        deducao = self.__salario * self.calcula_aliquota()
        return deducao   
