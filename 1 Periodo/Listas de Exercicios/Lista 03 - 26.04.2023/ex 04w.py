'''
4. Escreva um programa que imprime os N primeiros ímpares. Exemplo:
Quantos ímpares deseja?: 11
1 3 5 7 9 11 13 15 17 19 21
'''

numeroImpares = int(input('Escolha um valor para o número de ímpares: '))

numero = 1
contador = 1

while contador <= numeroImpares:
    print(numero, end=' ')
    numero += 2
    contador += 1

#github.com/tiagodefendi
