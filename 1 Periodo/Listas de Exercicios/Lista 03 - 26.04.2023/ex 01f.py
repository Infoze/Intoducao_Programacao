'''
1. Escreva um programa que faz a leitura de um valor N e imprime N linhas de texto exibindo o
número da linha corrente. Exemplo:
Informe o número de linhas: 10
Linha 1
Linha 2
Linha 3
...
Linha 10
'''

numeroLinhas = int(input('Escolha um valor para o número de linhas: '))

for linhas in range(1, numeroLinhas+1):
    print(f'Linha nº {linhas}')

#github.com/tiagodefendi
