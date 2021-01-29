# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
12 1 5.30
16 2 5.10

Exemplos de Saída
VALOR A PAGAR: R$ 15.50
"""

linha1 = input().split()
linha2 = input().split()

cod1, qtde1, valor1 = linha1
cod2, qtde2, valor2 = linha2

total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))

print(f'VALOR A PAGAR: R$ {total:.2f}')