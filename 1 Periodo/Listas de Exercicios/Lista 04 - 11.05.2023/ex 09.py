'''
9. Utilizando a função do exercício anterior, escreva uma função que imprime uma caixa, recebendo
como parâmetros:
a. Largura e altura da caixa (width e height);
b. O caractere de preenchimento da caixa (fill);
c. O caractere das bordas da caixa (edge).
Função: print_box(height: int, width: int, fill: str, edge: str)
Exemplo de uso:
print_box(5, 10, '#', 'o')
o--------o
|########|
|########|
|########|
o--------o
'''

def print_box(height:int, width:int, fill:str, vertex:str) -> str:
    for c in range(1, height* width+1):
        #vertex
        if (c == 1) or (c == width * height - width+1) or (c == height * width):
            print(f'{vertex}', end='')
        elif (c == width):
            print(f'{vertex}')
        #edge
        #
        elif (c // width == 0 or c // width == height - 1) and c%width != 0:
            print('-', end='')
        #
        elif c % width == 1:
            print('|', end='')

        elif c % width == 0:
            print('|')
        #fill
        else:
            print(f'{fill}', end='')
    print()

def main():
    print_box(5, 10, '#', 'o')
    print_box(3, 4, 'X', '@')
    print_box(1, 1, '#', 'o')
    print_box(10, 10, '#', 'o')
main()

#github.com/tiagodefendi
