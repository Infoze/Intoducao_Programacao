'''
9. Escreva um programa que lê três números e os escreve em ordem crescente.
'''

numero1 = int(input('Escolha um valor para o 1º número'))
numero2 = int(input('Escolha um valor para o 2º número'))
numero3 = int(input('Escolha um valor para o 3º número'))

maior = numero1
menor = numero1
meio = numero1

if maior < numero2:
    maior = numero2
if maior < numero3:
    maior = numero3
    
if menor > numero2:
    menor = numero2
if menor > numero3:
    menor = numero3 



#github.com/tiagodefendi
