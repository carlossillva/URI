# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
-5
0
-3
-4
12

Exemplos de Saída
3 valor(es) par(es)
2 valor(es) impar(es)
1 valor(es) positivo(s)
3 valor(es) negativo(s)
"""
class numeros:
	def __init__(self, valores):
		self.valores = valores

	def numPar(self):
		par = 0
		for valor in self.valores:
			if valor % 2 == 0:
				par += 1
		return par


	def numImp(self):
		imp = 0
		for valor in self.valores:
			if valor % 2 != 0:
				imp += 1
		return imp


	def numPosi(self):
		posi = 0
		for valor in self.valores:
			if valor > 0:
				posi += 1
		return posi


	def numNega(self):
		nega = 0
		for valor in self.valores:
			if valor < 0:
				nega += 1
		return nega


dados = list()
for leia in range(5):
	dados.append(int(input()))

info = numeros(dados)

print(f'''{info.numPar()} valor(es) par(es)
{info.numImp()} valor(es) impar(es)
{info.numPosi()} valor(es) positivo(s)
{info.numNega()} valor(es) negativo(s)''')
