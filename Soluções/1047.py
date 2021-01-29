# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
7 8 9 10

Exemplos de Saída
O JOGO DUROU 2 HORA(S) E 2 MINUTO(S)
"""
def conversor(dados):

	hi, mi, hf, mf = dados
	# Trasnformando horas em minutos
	tot_minutos_ini = (hi * 60) + mi # > Somando 'mi' com minutos de 'hi' 
	tot_minutos_fin = (hf * 60) + mf # > Somando 'mf' com minutos de 'hf' 

	# Calculando a diferênça de minutos entre horarios..
	tot_minutos_dif = ((24 * 60) - tot_minutos_ini) + tot_minutos_fin 

	# Convertendo minutos em (h:m)
	horas = tot_minutos_dif // 60 # Quantidades em horas
	minutos = tot_minutos_dif % 60 # Quantidades em minutos

	#Condição cujo haver um estouro de tempo (h > 24)..
	if horas >= 24 and minutos >= 1:
		horas = horas % 24
	print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')


# Coletando Dados 
horarios = str(input()).split()

#Convertendo Dados str() >> int()
horas = list()
for item in horarios:
	horas.append(int(item))

conversor(horas)