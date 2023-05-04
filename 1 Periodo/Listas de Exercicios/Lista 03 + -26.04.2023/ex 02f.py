'''
2. Escreva um programa que imprime a tabela ASC com valores em decimal (%03d), hexadecimal
(%03X) e o caractere (%c). Imprima apenas os caracteres 33 ao 125, separados em 3 colunas
(cada uma conterá 31 elementos), similar ao seguinte exemplo:
DEC HEX CHR     DEC HEX CHR     DEC HEX CHR
033 021 !       064 040 @       095 061 _
034 022 "       065 041 A       096 062 `
035 023 #       066 042 B       097 063 a
036 024 $       067 043 C       098 064 b
...             ...             ...
061 03D =       092 05C \       123 07D {
062 03E >       093 05D ]       124 07E |
063 03F ?       094 05E ^       125 07F }
'''
print('DEC  HEX  CHR  |  DEC  HEX  CHR  |  DEC  HEX  CHR')
for caracter in range(33, 64):
    print(f'{caracter : >3} {hex(caracter) : >5} {chr(caracter) : >2}|{caracter+31 : >3} {hex(caracter+31) : >5} {chr(caracter+31) : >2}|{caracter+62 : >3} {hex(caracter+62) : >5} {chr(caracter+62) : >2}')

#github.com/tiagodefendi
