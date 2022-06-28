from src.business.cadastro import Cadastro
from src.entities.funcionario import Funcionario

f1 = Funcionario("Monique", "70341102121", (2022, 6, 30), "Cientista de Dados", "Sim")

cadastro = Cadastro()

cadastro.cadastrar_funcionario(f1)

print(f1.nome)
print(f1.data_admissao)
print(f1.matricula)
