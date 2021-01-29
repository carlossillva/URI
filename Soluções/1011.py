# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3

Exemplos de Saída
VOLUME = 113.097
"""
from math import pow

r = float(input())

pi = 3.14159 

volume = ((4 / 3) * (pi * pow(r, 3)))

print(f'VOLUME = {volume:.3f}')