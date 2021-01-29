# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
7.0 5.0 7.0

6.0 6.0 10.0

5.0 7.0 2.0

Exemplos de Saída
TRIANGULO ACUTANGULO
TRIANGULO ISOSCELES

TRIANGULO OBTUSANGULO
TRIANGULO ISOSCELES

NAO FORMA TRIANGULO
"""
from math import pow

def tipos_triangulo(dados):

	valores = list()

	"""CONVERTENDO DADOS PARA FLOAT"""
	for item in dados:
		valores.append(float(item))

	valores = sorted(valores, reverse=True) # VALORES EM DECRESCENTE
	a, b, c = valores
	
	# NAO FORMA TRIANGULO
	if a >= (b + c):
		print('NAO FORMA TRIANGULO')
	else:
		# TRIANGULO RETANGULO
		if pow(a, 2) == (pow(b, 2) + pow(c, 2)) :
			print('TRIANGULO RETANGULO')

		# TRIANGULO OBTUSANGULO
		if pow(a, 2) > (pow(b, 2) + pow(c, 2)):
			print('TRIANGULO OBTUSANGULO')

		# TRIANGULO ACUTANGULO
		if pow(a, 2) < (pow(b, 2) + pow(c, 2)):
			print('TRIANGULO ACUTANGULO')

		# TRIANGULO EQUILATERO
		if a == b and a == c:
			print('TRIANGULO EQUILATERO')

		# TRIANGULO ISOSCELES
		if a == b != c or b == c != a or c == b != a:
			print('TRIANGULO ISOSCELES')

# CHAMANDO FUNÇÃO..
tipos_triangulo(str(input()).split()) 
