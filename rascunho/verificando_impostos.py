from src.business.imposto_irrf import (aliquotas_INSS, aliquotas_IRRF,
                                       deducao_INSS, deducao_IRRF,
                                       remuneracao_INSS, remuneracao_IRRF)

from rascunho.imposto_calculo import Imposto

# valor de imposto inss descontado na folha de pagamento do funcionario especifico
x_inss = Imposto(aliquotas_INSS, remuneracao_INSS, deducao_INSS)
x_inss.contribuicao(base_de_calculo=5000)
