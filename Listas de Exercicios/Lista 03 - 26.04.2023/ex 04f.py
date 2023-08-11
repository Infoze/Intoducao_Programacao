'''
4. Escreva um programa que imprime os N primeiros ímpares. Exemplo:
Quantos ímpares deseja?: 11
1 3 5 7 9 11 13 15 17 19 21
'''

numeroImpares = int(input('Escolha um valor para o número de ímpares: '))

for numero in range(0, numeroImpares*2):
    if (numero % 2 == 1):
        print(numero, end=' ')

#github.com/tiagodefendi
