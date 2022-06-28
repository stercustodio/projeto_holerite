aliquotas_INSS = [0.075, 0.09, 0.12, 0.14]
remuneracao_INSS = [
            (0, 1_212),
            (1_212.01, 2_427.35),
            (2_427.36, 3_641.03),
            (3_641.04, 7_087.22)
            ]
deducao_INSS = [0, 18.18, 91, 163.82]



def contribuicao_inss(base_de_calculo_inss):
        
    if base_de_calculo_inss > remuneracao_INSS[-1][-1]:
        contribuicao = remuneracao_INSS[-1][-1] * aliquotas_INSS[-1] - deducao_INSS[-1]
    
    else:    
        if  base_de_calculo_inss < remuneracao_INSS[0][1]:
            aliquota = aliquotas_INSS[0]
            deducao = deducao_INSS[0]
        elif base_de_calculo_inss < remuneracao_INSS[1][1]:
            aliquota = aliquotas_INSS[1]
            deducao = deducao_INSS[1]
        elif base_de_calculo_inss < remuneracao_INSS[2][1]:
            aliquota = aliquotas_INSS[2]
            deducao = deducao_INSS[2]
        elif base_de_calculo_inss < remuneracao_INSS[3][1]:
            aliquota = aliquotas_INSS[3]
            deducao = deducao_INSS[3]
        contribuicao = base_de_calculo_inss * aliquota - deducao
    
    return round(contribuicao, 2)

# teste
lista = [
contribuicao_inss(1_000),
contribuicao_inss(1_500),
contribuicao_inss(2_900),
contribuicao_inss(6_900),
]
print(lista)
