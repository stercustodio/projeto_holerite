from src.entities.cargo import Cargo
from src.entities.funcionario import Funcionario

from rascunho.inss import INSS
from rascunho.tabela_cargo import tabela_cargo


def cargo(funcionario: Funcionario) -> object:
  cargo_do_funcionario = list(filter(lambda x: funcionario.cargo == x.codigo, tabela_cargo))[-1]
  return cargo_do_funcionario
      
def salario(funcionario: Funcionario) -> float:
  return cargo(funcionario).salario_base
          
def percentual_comissao(funcionario: Funcionario) -> float:
  if funcionario.comissao == True:
    return cargo().comissao
  else:
    return 0
      
def valor_comissao(funcionario: Funcionario) -> float:
  valor_comissao = salario() * percentual_comissao()
  return valor_comissao

def base_calc_INSS(funcionario: Funcionario):
   return salario()
      
def base_calc_IRRF(funcionario: Funcionario):
  return (salario() + valor_comissao() - INSS.parcela_a_deduzir())
