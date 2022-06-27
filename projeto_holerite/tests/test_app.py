import app
import pytest
from src.business.cadastro_funcionario import CadastroFuncionario


@pytest.fixture()
def funcionario():
    app.cadastro_funcionario = CadastroFuncionario()
    return app.app.test_funcionario()


def test_inserir_funcionario():
    # Dado
    # Quando
    response = funcionario.post("/funcionario", json={
            "matricula": "123456",
            "nome": "Joaquina",
            "cpf": "100.200.300-10",
            "data_admissao": "12/03/2012",
            "cargo": 32,
            "comissao": True 
        })

    # Entao
    assert response.status_code == 201


def test_busca_funcionarios():
    # Dado
    # Quando
    response =funcionario.get("/funcionario")

    # Entao
    assert response.json == []


def test_busca_funcionarios():
    # Dado
    # Quando
    response = funcionario.get("/funcionario")

    # Entao
    assert response.status_code == 200


def test_busca_funcionario_404(client):
    # Dado
    # Quando
    response = funcionario.get("/funcionario/123")

    # Entao
    assert response.status_code == 404


def test_consultar_funcionario(funcionario):
    # Dado
    funcionario.post("/funcionario/1", json={
            "matricula": "123456",
            "nome": "Joaquina",
            "cpf": "100.200.300-10",
            "data_admissao": "12/03/2012",
            "cargo": 32,
            "comissao": True
        })
    
    funcionario.post("/funcionario/2", json={
            "matricula": "102030",
            "nome": "Jureminha",
            "cpf": "500.200.300-10",
            "data_admissao": "30/07/2019",
            "cargo": 30,
            "comissao": True 
        })

    # Quando
    response = funcionario.get("/funcionario/1")

    # Entao
    assert response.json == {
        "matricula": "123456",
        "nome": "Joaquina",
        "cpf": "100.200.300-10",
        "data_admissao": "12/03/2012",
        "cargo": 32,
        "comissao": True
    }


def test_remover_funcionario(funcionario):
    # Dado
    funcionario.post("/funcionario/1", json={
            "matricula": "123456",
            "nome": "Joaquina",
            "cpf": "100.200.300-10",
            "data_admissao": "12/03/2012",
            "cargo": 32,
            "comissao": True
        })
  
    funcionario.post("/funcionario/2", json={
            "matricula": "102030",
            "nome": "Jureminha",
            "cpf": "500.200.300-10",
            "data_admissao": "30/07/2019",
            "cargo": 30,
            "comissao": True 
        })

    # Quando
    funcionario.delete("/funcionario/1")

    # Entao
    response = funcionario.get("/funcionario/1")
    assert response.status_code == 404
