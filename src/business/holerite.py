from getpass import getpass
from typing import List

from mysql.connector import Error, connect
from src.business.imposto_inss import contribuicao_inss
from src.business.imposto_irrf import contribuicao_irrf
from src.business.tabelas import TABLES
from src.entities.cargo import Cargo
from src.entities.funcionario import Funcionario


class Holerite:
    
    def __init__(self, funcionario: Funcionario, DB_NAME):
        self.funcionario : Funcionario = funcionario
        self.tabela_cargo = DB_NAME
        
    def relacionamento(self) -> dict:
        
        descricao = 'select from tabela_cargo descricao when cargo.codigo = funcionario.cargo'
        salario_base = 'select from tabela_cargo salario_base when cargo.codigo = funcionario.cargo'
        comissao_percentual = 'select from tabela_cargo comissao when cargo.codigo = funcionario.cargo'
        comissao_valor = comissao_percentual * salario_base
        
        infos = {
            'descricao': descricao,
            'salario_base': salario_base,
            'comissao_percentual': comissao_percentual,
            'comissao_valor': comissao_valor
            }
        
        return infos

        
    def printar_dados_empresa(self) -> List[str]:
        dados_empresa = [
            '\nEmpresa XPTO Alimentos',
            '\nEndereço: Rua XV de Novembro, 15, Centro',
            '\nCNPJ: 12.345.678/0001-00',
            '\nRecibo de Pagamento de Salário',
            '\nMês de referência: Abril/2022'
        ]
        return dados_empresa
    
    def prinar_dados_funcionario(self) -> dict:
        
        dados_funcionario = {
            'Matrícula': self.funcionario.matricula,
            'Nome': self.funcionario.nome, 
            'Data de admissão': self.funcionario.data_admissao, 
            'Função': descricao
        }
        return dados_funcionario
        
    def printar_tabela(self, salario_base: float = 22.5, faltas: int = 0):
        tabela_holerite = {
            'Código': [101, 203, 303, 973, 978],
            'Descrição': ["salario base", "comissao", "faltas", "inss folha", "irrf folha"],
            'Referência': [
                salario_base,
                Holerite.relacionamento()['comissao_percentual'],
                faltas,
                contribuicao_inss(self.funcionario),
                contribuicao_irrf(self.funcionario)
                ],
            'Proventos': [
                Holerite.relacionamento()['salario_base'], 
                Holerite.relacionamento()['comissao_valor']
            ],
        }

    def printar_ultima_linha(self):
        
        ultima_linha = {
            'Base INSS': (salario_base + valor_comissao)
        }
        
        return ultima_linha
