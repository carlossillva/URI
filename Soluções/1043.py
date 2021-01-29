# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
6.0 4.0 2.0

6.0 4.0 2.1

Exemplos de Saída
Area = 10.0

Perimetro = 12.1
"""
a, b, c = str(input()).split()

if (float(b) - float(c)) < float(a) and float(a) < (float(b) + float(c)):
	perimetro = float(a) + float(b) + float(c)
	print(f'Perimetro = {perimetro:.1f}')
else:
	area = ((float(a) + float(b)) * float(c)) / 2
	print(f'Area = {area:.1f}')