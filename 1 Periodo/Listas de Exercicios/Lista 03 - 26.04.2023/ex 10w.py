'''
10. Escreva um programa que calcula a divisão inteira e o resto de dois números inteiros utilizando
somente o operador aritmético de subtração (-). O programa deve informar o quociente e o resto.
Exemplo:
Informe a / b: 9 2
9/2 = 4
9%2 = 1
'''

numero = int(input('Escolha um valor para o número: '))
divisor = int(input(f'Escolha um valor para dividir {numero}: '))

divisao = numero
inteiro = 0
resto = 0

while divisao - divisor > 0:
    divisao -= divisor
    inteiro += 1
resto = divisao


print(f'{numero} // {divisor} = {inteiro}')
print(f'{numero} % {divisor} = {resto}')

#github.com/tiagodefendi
