# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
11

Exemplos de Saída
Sao Paulo
"""
ddd = {
	61:'Brasilia',
	71:'Salvador',
	11:'Sao Paulo',
	21:'Rio de Janeiro',
	32:'Juiz de Fora',
	19:'Campinas',
	27:'Vitoria',
	31:'Belo Horizonte'
}

try:
	print(ddd[int(input())])
except KeyError:
	print('DDD nao cadastrado')