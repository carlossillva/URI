# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
16 2

Exemplos de Saída
O JOGO DUROU 10 HORA(S)
"""
hora_inicio, hora_fim = str(input()).split()

hora_inicio = int(hora_inicio)
hora_fim = int(hora_fim)

if hora_inicio > hora_fim:
	duracao = ((24 - hora_inicio) + hora_fim)
elif hora_inicio == hora_fim:
	duracao = 24
elif hora_inicio < hora_fim:
	duracao = ((hora_inicio - hora_fim) * -1)

print(f'O JOGO DUROU {duracao} HORA(S)')
