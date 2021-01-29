# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
7 14 106

Exemplos de Saída
106 eh o maior
"""

a, b , c = str(input()).split()

maior = (int(a) + int(b) + abs(int(a) - int(b))) / 2
ressultado = (int(maior) + int(c) + abs(int(maior) - int(c))) / 2

print(f'{ressultado:.0f} eh o maior')