# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
3002.00

1701.12

Exemplos de Saída
R$ 80.36

Isento
"""
renda = {
	'isento':[0, 2000.00],
	8:[2000.01, 3000.00],
	18:[3000.01, 4500.00],
	28:[4500.00]
}

salario = float(input())

for chave, valor in renda.items():
	if len(valor) == 2:
		if salario >= valor[0] and salario <= valor[1]:
			if chave == 'isento':
				print('Isento')
				break
			else:
				if chave == 8:
					imposto = (salario - 2000) * (8 / 100)
					print(f'R$ {imposto:.2f}')
					break
				elif chave == 18:
					isento = salario - 2000
					por8 = 1000
					por18 = isento - 1000
					imposto = ((8 / 100) * por8) + ((18 / 100) * por18)
					print(f'R$ {imposto:.2f}')
					break				
	else:
		por8 = 1000 
		por18 = 1500
		por28 = salario - 4500
		imposto = ((8 / 100) * por8) + ((18 / 100) * por18) + ((28 / 100) * por28)
		print(f'R$ {imposto:.2f}')