'''
10. Escreva um programa que imprime uma caixa de caracteres com as dimensões informadas. O
programa deve ler o caractere, bem como, as dimensões da caixa (largura e altura). Você só pode
usar 1 laço (não deve usar laços aninhados, isto é, laço dentro de laço). Também não pode
utilizar operadores e funções de strings.
Exemplo:
Caractere: X
Lagura: 5
Altura: 3
XXXXX
XXXXX
XXXXX
'''

caracter = input('Escolha um caracter para montar uma caixa: ')
largura = int(input('Escolha um valor para a largura: '))
altura = int(input('Escolha um valor para a altura: '))

for contador in range(0, altura):
    print(caracter*largura)

#github.com/tiagodefendi
