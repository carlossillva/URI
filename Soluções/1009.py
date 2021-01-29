# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
JOAO
500.00
1230.30

Exemplos de Saída
TOTAL = R$ 684.54
"""

def fucionario(nome='Desconlhecido', salario=645.58, montante=0, comissao=0):

	bonus = (montante * (comissao / 100))
	novo_salario = bonus + salario

	print(f'TOTAL = R$ {novo_salario:.2f}')


nome = str(input()).strip().upper()
salario = float(input())
montante = float(input())

fucionario(nome, salario, montante, comissao=15)

