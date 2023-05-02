'''
1. Escreva um programa que faz a leitura de um valor N e imprime N linhas de texto exibindo o
número da linha corrente. Exemplo:
Informe o número de linhas: 10
Linha 1
Linha 2
Linha 3
...
Linha 10

----------------------------------------------------------------------------------------------

2. Crie uma variação do programa anterior de forma que ele imprima as linhas em contagem
decrescente. Exemplo:
Informe o número de linhas: 10
Linha 10
Linha 9
Linha 8
...
Linha 1
'''

numeroLinhas = int(input('Escolha um valor para o número de linhas: '))

for linhas in range(numeroLinhas, 0, -1):
    print(f'Linha nº {linhas}')

#github.com/tiagodefendi
