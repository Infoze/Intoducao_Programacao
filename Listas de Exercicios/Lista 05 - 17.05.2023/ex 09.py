'''
9. Escreva uma função que exibe um triângulo centralizado formado por caracteres "[]", com m
caracteres de altura.
Função: def centered_triangle(m: int, n: int)
Para m=6:
     []
    [][]
   [][][]
  [][][][]
 [][][][][]
[][][][][][]
'''

def centered_triangle(height:int):
    for i in range(height):
        for empty in range(height, 0, -1):
            if empty > i:
                print(' ', end='')
        for j in range(height-(height - i) + 1):
            print('🟧', end='')
        print()
    print()

def main():
    centered_triangle(6)
    centered_triangle(3)
main()

#github.com/tiagodefendi
