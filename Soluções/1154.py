# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
34
56
44
23
-2

Exemplos de Saída
39.25
"""
idades = list()

while True:
	idade = int(input())
	if idade >= 0:
		idades.append(idade)
	else:
		media = sum(idades) / len(idades)
		break
print(f'{media:.2f}')