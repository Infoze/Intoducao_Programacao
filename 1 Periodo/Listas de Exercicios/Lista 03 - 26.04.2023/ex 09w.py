'''
9. Escreva um programa que calcula a multiplicação de dois números inteiros utilizando somente o
operador aritmético de adição (+).
Exemplo:
Informe a x b: 5 7
5x7 = 35
'''

numero = int(input('Escolha um valor para o número: '))
vezes = int(input(f'Escolha um valor para multiplicar {numero}: '))

multiplicacao = 0

contador = 1

while contador <= vezes:
    multiplicacao += numero
    contador += 1

print(f'{numero} x {vezes} = {multiplicacao}')

#github.com/tiagodefendi
