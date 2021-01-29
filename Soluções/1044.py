# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
6 24

6 25

Exemplos de Saída
Sao Multiplos

Nao sao Multiplos
"""
a, b = str(input()).split()

if int(b) % int(a) == 0 or int(a) % int(b) == 0:
	print('Sao Multiplos')
else:
	print('Nao sao Multiplos')