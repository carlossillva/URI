# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
576.73

Exemplos de Saída
NOTAS:
5 nota(s) de R$ 100.00
1 nota(s) de R$ 50.00
1 nota(s) de R$ 20.00
0 nota(s) de R$ 10.00
1 nota(s) de R$ 5.00
0 nota(s) de R$ 2.00
MOEDAS:
1 moeda(s) de R$ 1.00
1 moeda(s) de R$ 0.50
0 moeda(s) de R$ 0.25
2 moeda(s) de R$ 0.10
0 moeda(s) de R$ 0.05
3 moeda(s) de R$ 0.01
"""
# Notas 100, 50, 20, 10, 5, 2
# Moedas 1, 0.50, 0.25, 0.10, 0.05, 0.01

valor = float(input())

#Cedulas de 100
cedula_100 = int(valor // 100)
valor -= cedula_100 * 100

#Cedulas de 50
cedula_50 = int(valor // 50)
valor -= cedula_50 * 50

#Cedulas de 20
cedula_20 = int(valor // 20)
valor -= cedula_20 * 20

#Cedula de 10
cedula_10 = int(valor // 10)
valor -= cedula_10 * 10

#Cedulas de 5
cedula_5 = int(valor // 5)
valor -= cedula_5 * 5

#Cedula de 2
cedula_2 = int(valor // 2)
valor -= cedula_2 * 2

#Moedas de 1
moeda_1 = int(valor // 1)
valor -= moeda_1 * 1

#Moedas de 0.50
moeda_0_50 = int(valor // 0.50)
valor -= moeda_0_50 * 0.50

#Moedas de 0.25
moeda_0_25 = int(valor // 0.25)
valor -= moeda_0_25 * 0.25

#Moedas de 0.10
moeda_0_10 = int(valor // 0.10)
valor -= moeda_0_10 * 0.10

#Moedas de 0.05
moeda_0_05 = int(valor // 0.05)
valor -= moeda_0_05 * 0.05

print(valor)

#Moedas de 0.01
moeda_0_01 = int(valor // 0.01)
valor -= moeda_0_01 * 0.01

print(f'''NOTAS:
{cedula_100} nota(s) de R$ 100.00
{cedula_50} nota(s) de R$ 50.00
{cedula_20} nota(s) de R$ 20.00
{cedula_10} nota(s) de R$ 10.00
{cedula_5} nota(s) de R$ 5.00
{cedula_2} nota(s) de R$ 2.00
''')

print(f'''MOEDAS:
{moeda_1} moeda(s) de R$ 1.00
{moeda_0_50} moeda(s) de R$ 0.50
{moeda_0_25} moeda(s) de R$ 0.25
{moeda_0_10} moeda(s) de R$ 0.10
{moeda_0_05} moeda(s) de R$ 0.05
{moeda_0_01} moeda(s) de R$ 0.01''')