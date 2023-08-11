'''
5. Escreva um programa que imprime todas as letras do alfabeto (minúscula e maiúscula), segundo o
exemplo:
LETRAS DO ALFABETO:
a | A
b | B
c | C
...
'''

for letra in range(97, 123):
    print(f'{chr(letra)} | {chr(letra-32)}')

#github.com/tiagodefendi
