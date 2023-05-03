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

contador = 1

while contador <= numeroLinhas:
    print(f'Linha {contador}')
    contador += 1

#github.com/tiagodefendi
