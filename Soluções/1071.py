# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
6
-5

Exemplos de Saída
5
"""
def soma_impares(x, y):

	maior = x if x > y else y
	menor = y if y < x else x

	menor += 1
	soma = 0

	while(menor < maior):
		if(menor % 2 != 0):
			soma += menor
		menor += 1
	return soma

valorX = int(input())
valorY = int(input())


print(soma_impares(valorX, valorY))
