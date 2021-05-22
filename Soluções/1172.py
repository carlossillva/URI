# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
0
-5
63
0
...

Exemplos de Saída
X[0] = 1
X[1] = 1
X[2] = 63
X[3] = 1
...
"""

vetor = list()
for c in range(1, 11):
	try:
		values = int(input())
		if values <= 0:
			vetor.append(1)
		else:
			vetor.append(values)
	except:
		vetor.append(1)
		continue

for key, values in enumerate(vetor):
	print(f'X[{key}] = {values}')