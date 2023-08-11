'''
8. Escreva um programa que calcula o fatorial de um número natural. Por definição: 0! = 1 e 1! = 1
Exemplo:
Informe o número: 5
5! = 1 x 2 x 3 x 4 x 5 = 120
'''

numero = int(input('Escolha um valor para o fatorial: '))
fatorial = 1

while numero > 0:
    fatorial *= numero
    print(numero, end=' ')
    if numero > 1:
        print('x', end=' ')
    else:
        print('=', end=' ')
    numero -= 1
print(fatorial)

#github.com/tiagodefendi
