'''
2. Escreva um programa que lê um número x do terminal e informa seu valor absoluto |x|, isto é:
a. |x| = x, se x > 0
b. |x| = -x, se x < 0
'''

numero = int(input('Escolha um valor para o número: '))

numeroAbsoluto = numero
if numero < 0:
    numeroAbsoluto = numero * -1

print(f'O valor absoluto de {numero} é igual a |{numeroAbsoluto}|')

#github.com/tiagodefendi
