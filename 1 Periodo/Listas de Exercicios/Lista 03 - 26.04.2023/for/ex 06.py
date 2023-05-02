'''
6. Escreva um programa que imprime a tabela ASC com valores em decimal (%d), octal (%o),
hexadecimal (%X) e o caractere (%c). Imprima apenas os caracteres 33 ao 126.
Exemplo:
DEC OCT HEX CHR
033 041 021 !
034 042 022 "
035 043 023 #
036 044 024 $
...
125 175 07D }
126 176 07E ~
'''

print('DEC  OCT  HEX  CHR')
for caracter in range(33, 127):
    print(f'{caracter : >3} {oct(caracter ) : >5} {hex(caracter) : >4} {chr(caracter)}')


#github.com/tiagodefendi
