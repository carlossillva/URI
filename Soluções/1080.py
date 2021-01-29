# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
2
113
45
34565
6
...
8

Exemplos de Saída
34565
4
"""
dados = list()

for leia in range(100):
	dados.append(int(input()))

maior = max(dados)
indice = dados.index(maior)

print(f'''{maior}
{indice+1}''')