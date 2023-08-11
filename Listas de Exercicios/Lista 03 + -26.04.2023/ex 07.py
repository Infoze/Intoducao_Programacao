'''
7. Escreva um programa que, dado dois números inteiros positivos (A e B), imprime o MDC (Máximo
Divisor Comum) entre ambos. O MDC é o maior número que divide A e B (divisão exata, de resto
zero). Dica: o máximo divisor comum entre A e B está, necessariamente, entre 2 e o menor entre A
e B, isto é, MENOR(A, B). Se você não encontrar um divisor comum entre A e B, então MDC = 1.
Informe os numeros: 30 12
> Maximo divisor comum: 6
Observe o processo
------------------
Divisores de 30: 1, 2, 3, 5, 6, 10, 15, 30
Divisores de 12: 1, 2, 3, 4, 6, 12
^ MDC
'''

numero1 = int(input('Escolha um valor para o 1º número: '))
numero2 = int(input('Escolha um valor para o 2º número: '))

contador = 1
mdc = 0

menor = numero1
if numero2 < menor:
    menor = numero2

while contador <= menor:
    if numero1 % contador == 0 and numero2 % contador == 0:
        mdc = contador
    contador += 1

print(f'O Máximo Divisor Comum de {numero1} e {numero2} é {mdc}')

#github.com/tiagodefendi
