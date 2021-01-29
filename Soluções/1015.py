# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
1.0 7.0
5.0 9.0

Exemplos de Saída
4.4721
"""
from math import sqrt, pow

x1, y1 = str(input()).split()
x2, y2 = str(input()).split()

distancia = sqrt(pow(float(x2) - float(x1), 2) + pow(float(y2) - float(y1), 2))

print(f'{distancia:.4f}')