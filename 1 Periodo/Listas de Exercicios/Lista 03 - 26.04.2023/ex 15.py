'''
15. Escreva um programa que exibe o primeiro e o último dígitos de um número inteiro. Exemplo:
Informe o número: 12405
> Primeiro: 1
> Último : 5
'''

numero = int(input('Escolha um valor para o número: '))

digitoFinal = numero % 10
digitoInicio = 0

while numero % 10 != 0 or numero // 10 > 0:
    if numero // 10 == 0:
        digitoInicio = numero
    numero //= 10
print(f'O primeiro dígito é {digitoInicio} e o último é {digitoFinal}')

#github.com/tiagodefendi
