'''
5. Escreva um programa que imprime todas as letras do alfabeto (minúscula e maiúscula), segundo o
exemplo:
LETRAS DO ALFABETO:
a | A
b | B
c | C
...
'''

letra = 97

while letra <= 122:
    print(f'{chr(letra)} | {chr(letra-32)}')
    letra += 1

#github.com/tiagodefendi
