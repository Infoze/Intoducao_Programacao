'''
5. Escreva um programa que, dado um número inteiro positivo, verifica se o mesmo é um Número
Perfeito. Um número perfeito é igual à soma de seus divisores positivos. Exemplo: 6 = 1 + 2 + 3,
Informe o numero: 6
Divisores de 6: 1 + 2 + 3 = 6
Numero perfeito? Sim
'''

numero = int(input('Escolha um valor para o número: '))

soma = 0

print(f'{numero}: ')

divisor = 1
while divisor < numero:
    if numero % divisor == 0:
        print(divisor, end=' + ')
        soma += divisor
    divisor += 1
print(f'\b\b= {soma}')

if soma == numero:
    print(f'O número {numero} é perfeito')
else:
    print(f'O número não é perfeito')

#github.com/tiagodefendi
