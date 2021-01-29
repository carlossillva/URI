# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
400.00

Exemplos de Saída
Novo salario: 460.00
Reajuste ganho: 60.00
Em percentual: 15 %
"""
tabela_salarios = {
	15:[0, 400.00],
	12:[400.01, 800.00],
	10:[800.01, 1200.00],
	7:[1200.01, 2000.00],
	4:[2000]
}

salario = float(input())

for perc, item in tabela_salarios.items():
	if len(item) == 2:
		if salario >= item[0] and salario <= item[1]:
			novo_salario = salario + ((perc / 100) * salario)
			reajuste = novo_salario - salario
			break
	else:
		novo_salario = salario + ((perc / 100) * salario)
		reajuste = novo_salario - salario		

print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {perc} %')
