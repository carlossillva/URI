# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
5 2
6 3
5 0

Exemplos de Saída
2 3 4 5 Sum=14
3 4 5 6 Sum=18
"""
def seqsoma(m, n):
	maior = m if m > n else n
	menor = n if n < m else m
	seq = list(range(menor, maior+1))
	soma = sum(seq)
	seq = str(seq[:]).strip('[]').replace(",", "")
	print(f'{seq} Sum={soma}')


while True:
	m, n = str(input()).split()
	m = int(m)
	n = int(n)
	if m <= 0 or n <= 0:
		break
	seqsoma(m, n)
