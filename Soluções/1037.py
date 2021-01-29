# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
25.01

Exemplos de Saída
Intervalo (25,50]
"""
# Intervalos
	#  0 a 25
	# 25 a 50
	# 50 a 75
	# 75 a 100

key = 0

def interv(x):
					#0		  #1		#2		  #3
	intervalos = [[0, 25], [25, 50], [50, 75], [75, 100]]

	global key

	for key, item in enumerate(intervalos):
		if x >= item[0] and x <= item[1]:

			return True


saida_intervalos = ('[0,25]', '(25,50]', '(50,75]', '(75,100]')

x = float(input())

if interv(x):
	print(f'Intervalo {saida_intervalos[key]}')
else:
	print('Fora de intervalo')
