from flask import Blueprint, Response, jsonify, request
from src.business.cadastro_funcionario import CadastroFuncionario
from src.entities.funcionario import Funcionario
from src.exceptions.funcionario_not_found_error import FuncionarioNotFoundError

funcionario = Blueprint('funcionario', __name__)

cadastro_funcionario = CadastroFuncionario()


@funcionario.route("/funcionario", methods=['POST'])
def inserir_funcionario():
    dados = request.json

    funcionario = Funcionario(
        "",
        dados['matricula'],
        dados['nome'],
        dados['cpf'],
        dados['data_admissao'],
        dados['cargo'],
        dados['comissao'])
    
    cadastro_funcionario.inserir(funcionario)

    return Response("ok", 201, {"x-codigos": "python"})


@funcionario.route("/funcionario/consultar", methods=['GET'])
def consultar_funcionario():
    funcionario = cadastro_funcionario.listar_todos()

    resultado = list(map(lambda x: {
        "matricula": x.matricula,
        "nome": x.nome,
        "cpf": x.cpf,
        "data_admissao": x.data_admissao,
        "cargo": x.cargo,
        "comissao": x.comissao
        },
        funcionario))

    return jsonify(resultado)


@funcionario.route("/funcionario/<nome>")
def consultar_funcionario(nome):
    try:
        funcionario = cadastro_funcionario.consultar(id)
    except FuncionarioNotFoundError:
        return "Not Found", 404

    resultado = {
        "id": funcionario.id,
        "endereco": funcionario.endereco,
        "telefone": funcionario.telefone,
        "cpf": funcionario.cpf,
        "nome": funcionario.nome
    }

    return jsonify(resultado)

@funcionario.route("/funcionario/<matricula>", methods=['DELETE'])
def delete_funcionario(matricula):
    cadastro_funcionario.remover_matricula(matricula)
    return "", 204
