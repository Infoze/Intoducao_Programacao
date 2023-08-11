'''
2. Dados dois parâmetros naturais m e n (linhas x colunas), escreva uma função que exibe um
retângulo formado por caracteres "[]", com mxn caracteres.
Função: def rect(m: int, n: int)
Para m=3 e n=6:
[][][][][][]
[][][][][][]
[][][][][][]
'''

def rect(height:int, width:int):
    for i in range(height):
        for j in range(width):
            print('🟧', end='')
        print()
    print()

def main():
    rect(3, 4)
    rect(5, 5)
main()

#github.com/tiagodefendi
