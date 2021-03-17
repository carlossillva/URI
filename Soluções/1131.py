# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3 2
1
2 3
1
3 1
2

Exemplos de Saída
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
Novo grenal (1-sim 2-nao)
3 grenais
Inter:2
Gremio:1
Empates:0
Inter venceu mais
"""

def grenal(i, g, gre, emp):
	print(f'{gre} grenais')
	print(f'Inter:{i}')
	print(f'Gremio:{g}')
	print(f'Empates:{emp}')
	print(f'{"Inter" if i > g else "Gremio"} venceu mais')


grenais = inter = empate = gremio = 0
while True:
	i, g = str(input()).split()
	i, g = int(i), int(g)
	grenais += 1
	if i > g:
		inter += 1
	elif g > i:
		gremio += 1
	else:
		empate += 1

	while True:
		print('Novo grenal (1-sim 2-nao)')
		fluxo = str(input())
		if fluxo not in '12':
			continue
		else:
			break
	if fluxo == '2':
		grenal(inter, gremio, grenais, empate)
		break			