'''
8. Escreva um programa que lê quatro números e informa o maior digitado.
'''

numero1 = int(input('Escolha um valor para o 1º número: '))
numero2 = int(input('Escolha um valor para o 2º número: '))
numero3 = int(input('Escolha um valor para o 3º número: '))
numero4 = int(input('Escolha um valor para o 4º número: '))

maior = numero1

if maior < numero2:
    maior = numero2
if maior < numero3:
    maior = numero3
if maior < numero4:
    maior = numero4

print(f'O valor do maior número digitado é {maior}; Números: {numero1}; {numero2}; {numero3}; {numero4}')

#github.com/tiagodefendi
