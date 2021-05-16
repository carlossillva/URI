# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3 99

Exemplos de Saída
1 2 3
4 5 6
7 8 9
10 11 12
...
97 98 99
"""
x, y = input().split(' ')
x, y = int(x), int(y)

newX = x
for num in range(1, y + 1):
    if num == newX:
        print(num, end='')
        print()
        newX += x
    else:
        print(num, end=' ')