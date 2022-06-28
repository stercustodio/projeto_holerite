aliquotas_IRRF = [0.0, 0.075, 0.15, 0.225, 0.275]
remuneracao_IRRF = [
            (0, 1_903.88),
            (1_903.89, 2_826.65),
            (2_826.66, 3_751.05),
            (3_751.06, 4_664.68)
]
deducao_IRRF = [0, 142.80, 354.80, 636.13, 869.36]

def contribuicao_irrf(base_de_calculo_irrf):
    
    if  base_de_calculo_irrf < remuneracao_IRRF[0][1]:
        aliquota = aliquotas_IRRF[0]
        deducao = deducao_IRRF[0]
    elif base_de_calculo_irrf < remuneracao_IRRF[1][1]:
        aliquota = aliquotas_IRRF[1]
        deducao = deducao_IRRF[1]
    elif base_de_calculo_irrf < remuneracao_IRRF[2][1]:
        aliquota = aliquotas_IRRF[2]
        deducao = deducao_IRRF[2]
    elif base_de_calculo_irrf < remuneracao_IRRF[3][1]:
        aliquota = aliquotas_IRRF[3]
        deducao = deducao_IRRF[3]
    else:
        aliquota = aliquotas_IRRF[4]
        deducao = deducao_IRRF[4]
    
    contribuicao = base_de_calculo_irrf * aliquota - deducao
    
    return round(contribuicao, 2)

# teste

lista = [
    contribuicao_irrf(500),
    contribuicao_irrf(2_500),
    contribuicao_irrf(3_600),
    contribuicao_irrf(4_664.68),
    contribuicao_irrf(5_000),
    contribuicao_irrf(78_000)
]

print(lista)
