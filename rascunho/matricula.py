from random import randint


def gerar_matricula() -> int:
    '''Gera um número de matrícula com n dígitos'''
    
    n = 6
    range_start = 10**(n-1)
    range_end = (10**n)-1
    matricula = randint(range_start, range_end)
        
    return matricula

