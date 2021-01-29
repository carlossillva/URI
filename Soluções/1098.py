# -*- coding: utf-8 -*-

"""
Exemplos de Entrada

Exemplos de Saída
I=0 J=1
I=0 J=2
I=0 J=3
I=0.2 J=1.2
I=0.2 J=2.2
I=0.2 J=3.2
.....
I=2 J=?
I=2 J=?
I=2 J=?
"""
def printN(i, j):
	for c in range(1, 4):
		if i > 0 and i < 1.8 and i != 1:
			print(f'I={i:.1f} J={c+j:.1f}')
		else:
			print(f'I={i:.0f} J={c+j:.0f}')	


I = 0
J = 0
while True:
	printN(I, J)
	I += 0.2
	J += 0.2
	if I > 2:
		break
