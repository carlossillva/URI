# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
10
10 C
6 R
15 S
5 C
14 R
9 C
6 R
8 S
5 C
14 R

Exemplos de Saída
Total: 92 cobaias
Total de coelhos: 29
Total de ratos: 40
Total de sapos: 23
Percentual de coelhos: 31.52 %
Percentual de ratos: 43.48 %
Percentual de sapos: 25.00 %
"""
def laboratorio(dados):
	
	tot_cobaias = tot_coelhos = tot_sapos = tot_ratos = 0
	for item in dados:
		# Total Cobaias
		tot_cobaias += int(item[0])
		# Total Coelhos
		if item[1] == 'C':
			tot_coelhos += int(item[0])
		# Total Ratos
		elif item[1] == 'R':
			tot_ratos += int(item[0])
		# Total Sapos
		else:
			tot_sapos += int(item[0])

	por_co = (tot_coelhos / tot_cobaias) * 100
	por_ra = (tot_ratos / tot_cobaias) * 100
	por_sa = (tot_sapos / tot_cobaias) * 100

	print(f'''Total: {tot_cobaias} cobaias
Total de coelhos: {tot_coelhos}
Total de ratos: {tot_ratos}
Total de sapos: {tot_sapos}
Percentual de coelhos: {por_co:.2f} %
Percentual de ratos: {por_ra:.2f} %
Percentual de sapos: {por_sa:.2f} %''')


n = int(input())

dados = list()

for leia in range(n):
	dados.append(str(input()).split())

laboratorio(dados)
