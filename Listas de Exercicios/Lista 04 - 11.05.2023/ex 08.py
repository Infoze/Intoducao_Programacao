'''
8. Escreva uma função que imprime uma linha com duas “pontas”. A função receberá como
parâmetros: a largura da linha (n), o caractere de preenchimento da linha (fill) e o caractere das
pontas da linha (edge).
Função: print_line(n: int, fill: str, edge: str)
Exemplo de uso:
print_line(10, '-', '+') # Saída: +--------+
'''

def print_line(number:int, fill:str, edge:str):
    for c in range(number):
        if c == 0 or c == (number-1):
            print(f'{edge}', end='')
        else:
            print(f'{fill}', end='')
    print()

def main():
    print_line(10, '-', '+')
    print_line(20, '=', '|')
    print_line(3, '_', 'O')
main()

#github.com/tiagodefendi
