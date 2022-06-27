from src.business.cadastro_funcionario import CadastroFuncionario
from src.entities.funcionario import Funcionario

tabela_funcionario = CadastroFuncionario()

anamariasilva = Funcionario('Ana Maria Silva', '11111111100', '02/07/2019', 32, True)
bernardosantos = Funcionario('Bernardo Santos', '22222222200', '16/10/2017', 20, False)
daianasantandesousa = Funcionario('Daiana Santana de Sousa', '33333333300', '04/09/2002', 30, True)
felipecruz = Funcionario('Felipe Cruz', '44444444400', '28/06/2021', 31, True)
danielferreira = Funcionario('Daniel Ferreira', '55555555500', '10/10/2012', 32, False)
joanasilveirapacheco = Funcionario('Joana Silveira Pacheco', '66666666600', '14/08/2009', 50, True)


anamariasilva.matricula = 111111
bernardosantos.matricula = 222222
daianasantandesousa.matricula = 333333
felipecruz.matricula = 444444
danielferreira.matricula = 555555
joanasilveirapacheco.matricula = 666666

tabela_funcionario.inserir(anamariasilva)
tabela_funcionario.inserir(bernardosantos)
tabela_funcionario.inserir(daianasantandesousa)
tabela_funcionario.inserir(felipecruz)
tabela_funcionario.inserir(danielferreira)
tabela_funcionario.inserir(joanasilveirapacheco)
