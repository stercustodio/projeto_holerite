from typing import List

from src.entities.funcionario import Funcionario
from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError
from src.exceptions.not_found_error import NotFoundError


class CadastroFuncionario:
    
    def __init__(self):
        self.__lista_funcionario: List[Funcionario] = []

    def inserir(self, funcionario: Funcionario) -> None:
        return self.__lista_funcionario.append(funcionario)
    
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
    
    def remover_matricula(self, matricula: int) -> None:
        funcionario = self.consultar_matricula(matricula)
        self.__lista_funcionario.remove(funcionario)
        
    def remover_nome(self, nome: str) -> None:
        funcionario = self.consultar_nome(nome)
        self.__lista_funcionario.remove(funcionario)
        
    def listar_todos(self) -> List[Funcionario]:
        return self.__lista_funcionario
        