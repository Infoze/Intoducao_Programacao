'''
8. Escreva um programa que, dado dois números inteiros positivos (A e B), imprime o MMC (Mínimo
Múltiplo Comum) entre ambos. O MMC é o menor número que resulta da multiplicação de A e B
por um número (não necessariamente igual para ambos). Dica: o mínimo múltiplo comum entre A e
B pode ser encontrado verificando se algum múltiplo do MAIOR(A, B) é divisível pelo MENOR(A,
B). Sempre há um MMC entre dois números quaisquer.
Informe os numeros: 30 12
> Minimo multiplo comum: 60
Observe o processo
------------------
Múltiplos de 30: 30, 60, 90,120,150,...
Múltiplos de 12: 12, 24, 36, 48, 60,...
x1 x2 x3 x4 x5 ...
O MMC entre 30 e 12 é 60.
'''

numero1 = int(input('Escolha um valor para o 1º número: '))
numero2 = int(input('Escolha um valor para o 2º número: '))

contador = 1
mmc = 0

while mmc == 0:
    if contador % numero1 == 0 and contador % numero2 == 0:
        mmc = contador
    contador += 1

print(f'O Mínimo Multiplo Comum entre {numero1} e {numero2} é {mmc}')

#github.com/tiagodefendi
