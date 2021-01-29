# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23

Exemplos de Saída
3 dia(s)
22 hora(s)
1 minuto(s)
0 segundo(s)
"""
from math import pow

dia_inicial = int(str(input()).split()[1])
hora_inicial = str(input()).replace(" ", "").split(':')

dia_final = int(str(input()).split()[1])
hora_final = str(input()).replace(" ", "").split(':')

hora_ini, min_ini, seg_ini = hora_inicial
hora_fin, min_fin, seg_fin = hora_final

tot_segundos_1 = ((dia_inicial * 24) * pow(60, 2)) + (int(hora_ini) * pow(60, 2)) + (int(min_ini) * 60) + int(seg_ini)
tot_segundos_2 = ((dia_final * 24) * pow(60, 2)) + (int(hora_fin) * pow(60, 2)) + (int(min_fin) * 60) + int(seg_fin)


dif_segundos = tot_segundos_2 - tot_segundos_1

dias = dif_segundos // (24 * pow(60, 2))
dif_segundos -= dias * (24 * pow(60, 2))

horas = dif_segundos // pow(60, 2)
dif_segundos -= horas * pow(60, 2)

minutos = dif_segundos // 60
dif_segundos -= minutos * 60

segundos = dif_segundos

print(f'''{dias:.0f} dia(s)
{horas:.0f} hora(s)
{minutos:.0f} minuto(s)
{segundos:.0f} segundo(s)''')
