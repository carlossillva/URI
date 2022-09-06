# -*- coding: utf-8 -*-

def failure(*args):
    
    key, digits = args
    saida = digits.replace(key, '')

    if saida == '':
        saida = 0
    
    return int(saida)


while True:
    d, n = str(input()).split(' ')

    # Finalizando Programa
    if int(d) == 0 and int(n) == 0:
        break

    print(failure(d, n))
