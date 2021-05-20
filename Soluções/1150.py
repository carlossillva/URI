# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3
1
20
Exemplos de Saída
5
"""
def counte(x, y):
	soma = list()
	for c in range(x, y+1):
		soma.append(c)
		if sum(soma) > y:
			break
	return len(soma)


x = int(input())

while True:
	y = int(input())
	if y > x:
		print(counte(x, y))
		break
	else:
		continue