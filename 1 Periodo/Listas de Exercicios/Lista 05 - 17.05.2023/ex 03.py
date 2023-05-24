'''
3. Dados dois parâmetros naturais m e n, escreva uma função que exibe um retângulo torcido,
formado por caracteres "[]" e com mxn caracteres.
Função: def skewed_rect(m: int, n: int)
Para m=5 e n=4: [][][][]
[][][][]
  [][][][]
    [][][][]
      [][][][]
'''

def skewed_rect(height:int, width:int):
    for i in range(height):
        for empty in range(height):
            if empty < i:
                print('  ', end='')
        for j in range(width):
            print('🟧', end='')
        print()
    print()

def main():
    skewed_rect(3, 3)
    skewed_rect(5, 4)
main()

#github.com/tiagodefendi
