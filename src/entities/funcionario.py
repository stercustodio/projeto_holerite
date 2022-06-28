from random import randint


class Funcionario:

    def __init__(self, nome: str, cpf: str, data_admissao: str, cargo: str, comissao: bool):
        self.__matricula: int = randint(10**(6-1), (10**6)-1)
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__data_admissao: str = data_admissao
        self.__cargo: str = cargo
        self.__comissao: bool = comissao   
    
    @property
    def matricula(self) -> int:
        return self.__matricula        
    
    @property
    def nome(self) -> str:
        return self.__nome
    @nome.setter
    def nome(self, value) -> str:
        self.__nome = value
    
    @property
    def cpf(self) -> str:
        return self.__cpf
    @cpf.setter
    def cpf(self, value) -> str:
        self.__cpf = value

    @property
    def data_admissao(self) -> str:
        return self.data_admissao
    @data_admissao.setter
    def data_admissao(self, value) -> str:
        self.__data_admissao = value
    
    @property
    def cargo(self) -> str:
        return self.__cargo
    @cargo.setter
    def cargo(self, value) -> str:
        self.__cargo = value
        
    @property
    def comissao(self) -> bool:
        return self.__comissao
    @comissao.setter
    def comissao(self, value) -> bool:
        self.__comissao = value
