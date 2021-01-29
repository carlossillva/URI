# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3.0 4.0 5.2

Exemplos de Saída
TRIANGULO: 7.800
CIRCULO: 84.949
TRAPEZIO: 18.200
QUADRADO: 16.000
RETANGULO: 12.000
"""
from math import pow

a, b, c = input().split()

# Área do triângulo retângulo que tem A por base e C por altura.
area = (float(a) * float(c)) / 2

# Área do círculo de raio C. (pi = 3.14159)
pi = 3.14159
area_circulo = pi * pow(float(c), 2)

# Área do trapézio que tem A e B por bases e C por altura.
area_trapezio = ((float(a) + float(b)) * float(c)) / 2

# Área do quadrado que tem lado B.
area_quadrado = float(b) * float(b)

# Área do retângulo que tem lados A e B.
area_retangulo = float(a) * float(b)

print(f'''TRIANGULO: {area:.3f}
CIRCULO: {area_circulo:.3f}
TRAPEZIO: {area_trapezio:.3f}
QUADRADO: {area_quadrado:.3f}
RETANGULO: {area_retangulo:.3f}''')