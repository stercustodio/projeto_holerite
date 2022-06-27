from src.entities.funcionario import Funcionario

from rascunho.holerite import Holerite
from rascunho.inss import INSS


class IRRF:

    def __init__(self, funcionario: Funcionario):
        self.__aliquotas_IRRF = [0.0, 0.075, 0.15, 0.225, 0.275]
        self.__intervalo_remuneracao = [
            (0, 1_903.88),
            (1_903.89, 2_826.65),
            (2_826.66, 3_751.05),
            (3_751.06, 4_664.68),
            (4_664.69, 1_000_000.00)
            ]   
        self.__salario = Holerite.base_calc_IRRF()
        
    def calcula_aliquota(self) -> float:
        
        for i in range(4):
            if self.__salario in self.__intervalo_remuneracao[i]:
                aliquota = self.__aliquotas_IRRF[i]
                return aliquota
            
        if self.__salario > self.__intervalo_remuneracao[-1][1]:
            aliquota = self.__aliquotas_IRRF[-1]
            return aliquota
                
    def parcela_a_deduzir(self) -> float:
        deducao = self.__salario * self.calcula_aliquota()
        return deducao  
