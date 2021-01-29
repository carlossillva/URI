# -*- coding: utf-8 -*-

"""
Exemplos de Entrada

Exemplos de Saída
I=1 J=7
I=1 J=6
I=1 J=5
I=3 J=9
I=3 J=8
I=3 J=7
...
I=9 J=15
I=9 J=14
I=9 J=13
"""
i = 1
j = t = 7

while i < 10:
	for reduz in range(3):
		print(f'I={i} J={t}')
		t -= 1
	i += 2
	j += 2
	t = j 
