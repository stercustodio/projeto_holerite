from typing import List

from src.entities.cargo import Cargo


class CadastroCargo:
    
    def __init__(self):
        self.__lista_cargo: List[Cargo] = []
    
    def inserir(self, cargo: Cargo):
        self.__lista_cargo.append(cargo)
        
    def remover(self, cargo: Cargo):
        self.__lista_cargo.remove(cargo)
