from src.business.cadastro_funcionario import CadastroFuncionario
from src.entities.funcionario import Funcionario

anamariasilva = Funcionario('Ana Maria Silva', '11111111100', '02/07/2019', '32', True)
mariatereza = Funcionario('Maria Tereza Bastos', '200.200.100-20', '09/07/2003', '32', True)

anamariasilva.nome = 'Josefina Jureminha Oliveira'
anamariasilva.nome

anamariasilva.cpf = '20000000'
anamariasilva.cpf


tabela_funcionario = CadastroFuncionario()

tabela_funcionario.inserir(anamariasilva)
tabela_funcionario.inserir(mariatereza)

tabela_funcionario.consultar_matricula(anamariasilva.matricula)
tabela_funcionario.consultar_nome('Maria Tereza Bastos')
tabela_funcionario.listar_todos

tabela_funcionario.remover_matricula(anamariasilva.matricula)
tabela_funcionario.listar_todos

