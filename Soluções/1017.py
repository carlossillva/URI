# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
10
85

Exemplos de Saída
70.833
"""
km_h_gasolina = 12 # Litros ...

tempo_viagem = int(input()) # Em Horas...
km_h = int(input()) # Em km...

gasto_combustivel = (km_h * tempo_viagem) / km_h_gasolina

print(f'{gasto_combustivel:.3f}')