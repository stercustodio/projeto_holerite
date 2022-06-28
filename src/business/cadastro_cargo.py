from typing import List

import mysql.connector
from src.entities.cargo import Cargo


class CadastroCargo:
    
    def __init__(self):
        self.__lista_cargo: List[Cargo] = []
    
    def inserir(self, cargo: Cargo):
        
        cnx = mysql.connector.connect(user='stercustodio', password='senhaChata40*', host='127.0.0.1', database='projeto_holerite')
        cursor = cnx.cursor()
        
        inserir_cargo = (
            "INSERT INTO tabela_cargos "
            "(codigo, descricao, salario_base, comissao)"
            " VALUES (%(codigo)s, %(descricao)s, %(salario_base)s, %(comissao)s)"
            )

        cursor.execute(inserir_cargo, {
            "codigo": cargo.codigo,
            "descricao": cargo.descricao,
            "salario_base": cargo.salario_base,
            "comissao": cargo.comissao,          
        })
        cnx.commit()

        cursor.close()
        cnx.close()
    
    
    def consultar(self, codigo: int) -> Cargo:
       cargo = List(filter(lambda x: x.codigo == codigo, self.__lista_cargo))[-1]
       return cargo
            
    def remover(self, cargo: Cargo):
        self.__lista_cargo.remove(cargo)

    def listar_todos(self) -> List[Cargo]:
        return self.__lista_cargo
