# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
576

Exemplos de Saída
576
5 nota(s) de R$ 100,00
1 nota(s) de R$ 50,00
1 nota(s) de R$ 20,00
0 nota(s) de R$ 10,00
1 nota(s) de R$ 5,00
0 nota(s) de R$ 2,00
1 nota(s) de R$ 1,00
"""
# Notas 100, 50, 20, 10, 5, 2, 1

valor_info = valor = int(input())

cedula_100 = cedula_50 = cedula_20 = 0 
cedula_10 = cedula_5 = cedula_2 = cedula_1 = 0

while valor != 0:
	# Pegando todas as cédulas de 100
	if valor >= 100:
		valor -= 100
		cedula_100 += 1

	# Pegando todas as cédulas de 50
	elif valor >= 50:
		valor -= 50
		cedula_50 += 1

	# Pegando todas as cédulas de 20
	elif valor >= 20:
		valor -= 20
		cedula_20 += 1

	# Pegando todas as cédulas de 10
	elif valor >= 10:
		valor -= 10
		cedula_10 += 1

	# Pegando todas as cédulas de 5
	elif valor >= 5:
		valor -= 5
		cedula_5 += 1

	# Pegando todas as cédulas de 2
	elif valor >= 2:
		valor -= 2
		cedula_2 += 1

	# Pegando todas as cédulas de 1
	elif valor >= 1:
		valor -= 1
		cedula_1 += 1

print(f'''{valor_info}
{cedula_100} nota(s) de R$ 100,00
{cedula_50} nota(s) de R$ 50,00
{cedula_20} nota(s) de R$ 20,00
{cedula_10} nota(s) de R$ 10,00
{cedula_5} nota(s) de R$ 5,00
{cedula_2} nota(s) de R$ 2,00
{cedula_1} nota(s) de R$ 1,00''')
