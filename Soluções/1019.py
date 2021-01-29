# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
556

Exemplos de Saída
0:9:16
"""
segundos = int(input())

minutos = hora = 0

while True:
	if segundos >= 60:
		segundos -= 60
		minutos += 1

		if minutos == 60:
			hora += 1 
			minutos = 0

	else:
		break

print(f'{hora}:{minutos}:{segundos}')