# -*- coding: utf-8 -*-

"""
Exemplos de Entrada

Exemplos de Saída
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=7
I=3 J=6
I=3 J=5
...
I=9 J=7
I=9 J=6
I=9 J=5
"""
i = 1
j = 7

while i < 10:
	print(f'I={i} J={j}')
	j -= 1
	if j < 5:
		i += 2
		j = 7
		