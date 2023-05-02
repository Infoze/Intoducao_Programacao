'''
8. Escreva um programa que calcula o fatorial de um número natural. Por definição: 0! = 1 e 1! = 1
Exemplo:
Informe o número: 5
5! = 1 x 2 x 3 x 4 x 5 = 120
'''

numero = int(input('Escolha um valor para o fatorial: '))
multiplicacao = 1

print(f'{numero}! =', end=' ')
for fatorial in range(numero, 0, -1):
    print(fatorial, end='')
    if fatorial != 1:
        print(f' * ', end='')
    multiplicacao *= fatorial
print(f' = {multiplicacao}')

#github.com/tiagodefendi
