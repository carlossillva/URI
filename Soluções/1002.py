# -*- coding: utf-8 -*-

# Fórmula -> area = n * raio**2
# n = 3.14159

"""
Exemplos de Entrada
2.00

Exemplos de Saída
A=12.5664
"""
from math import pow

n = 3.14159
raio = float(input())

area = n * pow(raio, 2)

print(f'A={area:.4f}')
