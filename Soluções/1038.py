# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3 2

Exemplos de Saída
Total: R$ 10.00
"""
tabela_lanches = [
	['Cachorro Quente', 4.00],
	['X-Salada', 4.50],
	['X-Bacon', 5.00], 
	['Torrada simples', 2.00],
	['Refrigerante', 1.50]
]

codigo, quantidade = str(input()).split()

valor_lanche = tabela_lanches[int(codigo) - 1][1] * int(quantidade)

print(f'Total: R$ {valor_lanche:.2f}')