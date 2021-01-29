# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
400

Exemplos de Saída
1 ano(s)
1 mes(es)
5 dia(s)
"""
dados = int(input())
ano = mes = dias = 0
while True:

	if dados >= 365: #True, Temos 1 ano...
		ano += 1
		dados -= 365
		
	elif dados >= 30:
		mes += 1 # True, Temos um mes...
		dados -= 30
	else:
		dias = dados
		break

print(f'''{ano} ano(s)
{mes} mes(es)
{dias} dias(s)''')