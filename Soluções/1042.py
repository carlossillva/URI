# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
7 21 -14

Exemplos de Saída
-14
7
21

7
21
-14
"""
a, b, c = str(input()).split()

dados_input = (int(a), int(b), int(c))
crescente = sorted(dados_input)

for item1 in crescente:
	print(item1)
print()
for item2 in dados_input:
	print(item2)
