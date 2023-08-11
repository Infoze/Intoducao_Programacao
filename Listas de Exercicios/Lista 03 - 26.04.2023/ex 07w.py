'''
7. Escreva um programa que calcula o somatório de um número natural X fornecido pelo teclado.
Exemplo:
Informe o número: 5
1 + 2 + 3 + 4 + 5 = 15
'''

numero = int(input('Escolha um valor para a somatória: '))
soma = 0

while numero > 0:
    soma += numero
    print(numero, end=' ')
    if numero > 1:
        print('+', end=' ')
    else:
        print('=', end=' ')
    numero -= 1
print(soma)

#github.com/tiagodefendi
