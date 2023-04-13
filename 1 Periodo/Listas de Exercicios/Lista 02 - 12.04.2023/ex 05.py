'''
5. Escreva um programa que lê dois números naturais e informa o maior. O programa também deve
informar se os números são iguais. Caso o utilizador entre com números negativos, o programa
deve informar um erro e não realizar as demais verificações.
'''

numero1 = int(input('Escolha um valor para o 1º número: '))
numero2 = int(input('Escolha um valor para o 2º número: '))

if numero1 < 0 or numero2 < 0:
    print(f'ERRO! Somente números NATURAIS: {numero1}; {numero2}')
elif numero1 == numero2:
    print(f'Os números {numero1} e {numero2} são iguais')
elif numero1 > numero2:
    print(f'O número {numero1} é maior que {numero2}')
else:
    print(f'O número {numero2} é maior que {numero1}')

#github.com/tiagodefendi
