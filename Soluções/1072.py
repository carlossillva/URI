# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
4
14
123
10
-25

Exemplos de Saída
2 in
2 out
"""
def intervalo2(valores):
	intervalo = list(range(10, 21))
	inn = 0
	out = 0
	for valor in valores:
		if valor in intervalo:
			inn += 1
		else:
			out += 1
	return inn, out


x = int(input())

valores = list()

for leia in range(x):
	valores.append(int(input()))

inn, out = intervalo2(valores)

print(f'''{inn} in
{out} out''')