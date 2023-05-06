'''
12. Escreva um programa que imprime um triângulo de caracteres invertido com o número de linhas
informado. Você só pode usar 1 laço (não deve usar laços aninhados, isto é, laço dentro de
laço). Também não pode utilizar operadores e funções de strings.
Informe a quantidade de linhas: 5
XXXXX
XXXX
XXX
XX
X
'''

caracter = input('Escolha um valor para o carcter: ')
numero = int(input('Escolha um valor para o tamanho do triângulo: '))

for linha in range(numero, 0, -1):
    print(caracter * linha)

#github.com/tiagodefendi
