from typing import List

import mysql.connector
from src.entities.funcionario import Funcionario
from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError
from src.exceptions.not_found_error import NotFoundError


class CadastroFuncionario:
    
    def __init__(self):
        self.__lista_funcionario: List[Funcionario] = []

    def inserir(self, funcionario: Funcionario) -> None:
        cnx = mysql.connector.connect(user='stercustodio', password='senhaChata40*', host='127.0.0.1', database='projeto_holerite')
        cursor = cnx.cursor()
        inserir_funcionario = ("INSERT INTO tabela_funcionarios "
                            "(matricula, nome, cpf, data_admissao, cargo, comissao)"
                            " VALUES ( %(matricula)s, %(nome)s, %(cpf)s, %(data_admissao)s, %(cargo)s, %(comissao)s)")

        dados= {
            "matricula": funcionario.matricula,
            "nome": funcionario.nome,
            "cpf": funcionario.cpf,
            "data_admissao": funcionario.data_admissao,
            "cargo": funcionario.cargo,
            "comissao": funcionario.comissao            
        }
        
        cursor.execute(inserir_funcionario, dados)
        cnx.commit()
        cursor.close()
        cnx.close()
    
    
    def consultar_matricula(self, matricula: int) -> Funcionario:
        try:
            funcionario = list(filter(lambda x: x.matricula == matricula, self.__lista_funcionario))
            return funcionario[0]
        except NotFoundError:
            raise FuncionarioNotFoundError('Matrícula inválida')


    def consultar_nome(self, nome: str) -> Funcionario:
        try:
            funcionario = list(filter(lambda x: x.nome == nome, self.__lista_funcionario))        
            return funcionario[0]
        except NotFoundError:
            raise FuncionarioNotFoundError('Nome inválido')
    
    
    def remover_matricula(self, matricula: str) -> None:
        funcionario = self.consultar_matricula(matricula)
        
        resposta = input(f"Deseja mesmo excluir o funcionário {funcionario.matricula}? [S/N]")

        if resposta == 'S' or resposta == 's':
            self.__lista_funcionario.remove(funcionario)
            return ("Funcionário removido")
        else:
            print("Operação cancelada")


    def remover_nome(self, nome: str) -> None:
        funcionario = self.consultar_nome(nome)
        
        resposta = input(f"Deseja mesmo excluir o funcionário {funcionario.matricula}? [S/N]")

        if resposta == 'S' or resposta == 's':
            self.__lista_funcionario.remove(funcionario)
            return ("Funcionário removido")
        else:
            print("Operação cancelada")
       
        
    def listar_todos(self) -> List[Funcionario]:
        return self.__lista_funcionario
        
        # map(lambda x: print(x.nome), self.__funcionarios)
