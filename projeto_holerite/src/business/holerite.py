from typing import List

import mysql.connector
from src.entities.cargo import Cargo
from src.entities.funcionario import Funcionario
from src.entities.imposto_inss import contribuicao_inss
from src.entities.imposto_irrf import contribuicao_irrf
from src.entities.tabelas import TABLES


class Holerite:
    
    def __init__(self, funcionario: Funcionario, tabela_cargo: database):
        self.funcionario : Funcionario = funcionario
        self.tabela_cargo: database = tabela_cargo
        
    def relacionamento(self) -> dict:
        
        descricao = cargo.descricao
        salario_base = cargo.salario_base
        comissao_percentual = cargo.comissao
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
        descricao_funcao = ... 
        dados_funcionario = {
            'Matrícula': self.funcionario.matricula,
            'Nome': self.funcionario.nome, 
            'Data de admissão': self.funcionario.data_admissao, 
            'Função': descricao_funcao
        }
        return dados_funcionario
        
    def printar_tabela(self, salario_base: float = 22.5, faltas: int):
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
                Holerite.relacionamento()['valor_comissao']
            ],
        }

    def printar_ultima_linha(self):
        
        ultima_linha = {
            'Base INSS': (salario_base + valor_comissao)
        }
        
        return ultima_linha
