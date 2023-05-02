'''
11. Escreva um programa que faz a leitura de vários números inteiros (um a cada iteração do laço), até
que se digite zero. O programa deve imprimir a soma e a média aritmética simples dos números
digitados.
Exemplo:
Informes os números:
> 5
> 10
> 3
> 7
> 0
Soma: 25
Media: 6.25
'''

numero = int(input('Escolha um valor para o número: '))

soma = 0
contador = 0

while numero != 0:
    soma += numero
    contador += 1
    numero = int(input('Escolha um valor para o número: '))
media = soma / contador
print(f'A soma dos valores é {soma} e a média entre eles são {media}')

#github.com/tiagodefendi
