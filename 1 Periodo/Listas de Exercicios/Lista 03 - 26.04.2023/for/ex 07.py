'''
7. Escreva um programa que calcula o somatório de um número natural X fornecido pelo teclado.
Exemplo:
Informe o número: 5
1 + 2 + 3 + 4 + 5 = 15
'''

numero = int(input('Escolha um valor para a somatória: '))
soma = 0

for somatoria in range(1, numero+1):
    print(somatoria, end='')
    if somatoria != numero:
        print(f' + ', end='')
    soma += somatoria
print(f' = {soma}')

#github.com/tiagodefendi
