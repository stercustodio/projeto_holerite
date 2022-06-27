from flask import Blueprint, request
from src.business.cadastro_cargo import CadastroCargo
from src.entities.cargo import Cargo

cargo = Blueprint('cargo', __name__)


@cargo.route("/cargo", methods=["POST"])
def inserir_cargo():
    dados = request.json

    cargo = Cargo(
        "",
        dados['codigo'],
        dados['descricao'],
        dados['salario_base'],
        dados['comissao']
        )
        
    cadastro_cargo = CadastroCargo()

    cadastro_cargo.inserir(cargo)

    return "sucesso", 201
