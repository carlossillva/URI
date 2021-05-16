# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
8
1
7
2
2
4

Exemplos de Saída
MUITO OBRIGADO
Alcool: 1
Gasolina: 2
Diesel: 0
"""

a = g = d = 0

while True:
	opcao = int(input())
	if opcao == 4:
		break
	if opcao >= 1 or opcao < 4:
		if opcao == 1:
			a += 1
		elif opcao == 2:
			g += 1
		elif opcao == 3:
			d += 1
	else:
		continue 


print(f'''MUITO OBRIGADO
Alcool: {a}
Gasolina: {g}
Diesel: {d}''')

