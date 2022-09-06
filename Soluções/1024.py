# -*- coding: utf-8 -*-

def cripto(string):

    # Primeira etapa
    # --------------------------
    ascii_lista = list()
    for s in string:
        ascii_num = int(ord(s))
        if (
            ascii_num >= 65 and ascii_num <= 91 or
            ascii_num >= 97 and ascii_num <= 123
        ):
            ascii_num += 3
        
        ascii_lista.append(ascii_num)

    # Segunda etapa
    # -----------------------
    ascii_lista.reverse()

    # Terceira etapa
    # ------------------------
    tot_ascii = int(len(ascii_lista) / 2)

    ascii_final = list()
    
    for key, ascii_num in enumerate(ascii_lista):

        if key >= tot_ascii:
            ascii_num -= 1

        ascii_final.append(ascii_num)
    
    return ''.join(list(map(chr, ascii_final)))

loop = int(input())

for _ in range(0, loop):
    print(cripto(input()))
