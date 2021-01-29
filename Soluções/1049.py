# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
vertebrado
mamifero
onivoro

Exemplos de Saída
homem
"""
esquema = {
	
	'vertebrado':{
		'ave':{
			'carnivoro':'aguia',
			'onivoro':'pomba'
		}, 
		'mamifero':{
			'onivoro':'homem',
			'herbivoro':'vaca'
		}
	},

	'invertebrado':{
		'inseto':{
			'hematofago':'pulga',
			'herbivoro':'lagarta'
		}, 
		'anelideo':{
			'hematofago':'sanguessuga',
			'onivoro':'minhoca'
		}
	}
}

na = str(input())
nb = str(input())
nc = str(input())


print(esquema[na][nb][nc])