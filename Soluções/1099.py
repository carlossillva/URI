# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
7

4 5

13 10

6 4

3 3

3 5

3 4

3 8

Exemplos de Saída
0

11

5

0

0

0

12
"""
def soma_consecutivos(valores):
	x, y = valores
	x = int(x)
	y = int(y)
	maior = x if x > y else y
	menor = y if y < x else x

	menor += 1
	soma = 0

	while menor < maior:
		if menor % 2 != 0:
			soma += menor
		menor += 1
	return soma


n = int(input())

for leia in range(n):
	dados = str(input()).split()
	print(soma_consecutivos(dados))
