'''
13. Escreva um programa que imprime um triângulo de caracteres invertido, alinhado à direita, com o
número de linhas informado. Você só pode usar 1 laço (não deve usar laços aninhados, isto é,
laço dentro de laço). Também não pode utilizar operadores e funções de strings.
Informe a quantidade de linhas: 5
    X
   XX
  XXX
 XXXX
XXXXX
'''

caracter = input('Escolha um valor para o carcter: ')
numero = int(input('Escolha um valor para o tamanho do triângulo: '))

vazio = 1
limite = 1
linha = 1

while limite <= numero:
    if vazio <= numero-limite:
        print(' ', end='')
        vazio += 1
    elif linha % limite != 0:
        print(caracter, end='')
        linha += 1
    else:
        print(caracter)
        limite += 1
        linha = 1
        vazio = 1

#github.com/tiagodefendi
