# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
25
100
5.50

Exemplos de Saída
NUMBER = 25
SALARY = U$ 550.00
"""

def salario(n, h, v):
	
	salario = v * h
	
	print(f'NUMBER = {n}')
	print(f'SALARY = U$ {salario:.2f}')


number = int(input())
horas_trabalhadas = int(input())
valor_por_hora_trabalhada = float(input())

salario(number, horas_trabalhadas, valor_por_hora_trabalhada)