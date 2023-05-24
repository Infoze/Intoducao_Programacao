'''
4. Dados dois parâmetros naturais m e n, escreva uma função que exibe um retângulo torcido,
formado por caracteres "[]" e com mxn caracteres.
Função: def skewed_rect2(m: int, n: int)
Para m=5 e n=4: [][][][]
      [][][][]
    [][][][]
  [][][][]
[][][][]
'''

def skewed_rect2(height:int, width:int):
    for i in range(height, 0, -1):
        for empty in range(height, 0, -1):
            if empty < i:
                print('  ', end='')
        for j in range(width):
            print('🟧', end='')
        print()
    print()

def main():
    skewed_rect2(3, 3)
    skewed_rect2(5, 4)
main()

#github.com/tiagodefendi

