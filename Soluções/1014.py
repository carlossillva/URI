# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
500
35.0

Exemplos de Saída
14.286 km/l
"""
km = int(input())
combustivel = float(input())

consumo = km / combustivel

print(f'{consumo:.3f} km/l')