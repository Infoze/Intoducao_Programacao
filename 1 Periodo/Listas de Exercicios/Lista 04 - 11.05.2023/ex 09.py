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

def print_line(number:int, fill:str, edge:str):
    for c in range(number):
        if c == 0 or c == (number-1):
            print(f'{edge}', end='')
        else:
            print(f'{fill}', end='')
    print()

def print_box(height:int, width:int, fill:str, vertex:str) -> str:
    for c in range(1, height+1):
        #vertex
        if c == 1 or c == height:
            print_line(width, '-', vertex)
        #fill
        else:
            print_line(width, fill, '|')
    print()

def main():
    print_box(5, 10, '#', 'o')
    print_box(3, 4, 'X', '@')
    print_box(1, 1, '#', 'o')
    print_box(10, 10, '#', 'o')
main()

#github.com/tiagodefendi
