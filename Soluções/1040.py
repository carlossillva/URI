# -*- coding: utf-8 -*-

"""
Exemplos de Entrada
2.0 4.0 7.5 8.0
6.4

2.0 6.5 4.0 9.0

Exemplos de Saída
Media: 5.4
Aluno em exame.
Nota do exame: 6.4
Aluno aprovado.
Media final: 5.9

Media: 4.8
Aluno reprovado.
"""
class boletim:
	def __init__(self, notas):
		self.notas = notas
		self.media = 0.0


	def media_aluno(self):
		
		p1, p2, p3, p4 = [2, 3, 4, 1] # Pesos
		n1, n2, n3, n4 = self.notas # Notas
		self.media = ((float(n1)*p1) + (float(n2) * p2) + (float(n3) * p3) + (float(n4) * p4)) / 10
		print(f'Media: {self.media:.1f}')


	def situacao_aluno(self):

		if self.media >= 7.0:
			print('Aluno aprovado.')
		elif self.media < 5.0:
			print('Aluno reprovado.')
		elif self.media > 5.0 or self.media < 7.0:

			print('Aluno em exame.')
			nota_exame = float(input())
			print(f'Nota do exame: {nota_exame}')

			nova_media = (self.media + nota_exame) / 2
			
			if nova_media > 5.0:
				print('Aluno aprovado.')
			elif nova_media < 5.0:
				print('Aluno reprovado.')
			print(f'Media final: {nova_media:.1f}')


aluno = boletim(str(input()).split())
aluno.media_aluno()
aluno.situacao_aluno()
