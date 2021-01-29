# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
2200
1020
2022
2002

Exemplos de Saída
Senha Invalida
Senha Invalida
Senha Invalida
Acesso Permitido
"""
senha = '2002'
while True:
    dados = str(input())
    print(
        'Senha Invalida' if senha != dados else 'Acesso Permitido'
    )
    if dados == senha:
        break