"""
Exemplos de Entrada

Exemplos de Saída

"""

s = 0
n = 1
for c in range(1, 40, 2):
    s += c / n
    n = n * 2
print(f'{s:.2f}')