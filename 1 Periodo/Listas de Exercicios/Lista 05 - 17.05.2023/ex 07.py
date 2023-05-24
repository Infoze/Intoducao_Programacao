'''
7. Escreva uma função que exibe um triângulo retângulo formado por caracteres "[]", com m
caracteres de altura.
Função: def right_triangle(m: int)
Para m=5: [][][][][]
[][][][]
  [][][]
    [][]
      []
'''

def right_triangle(size:int):
    for i in range(size):
        for empty in range(size):
            if empty < i:
                print('  ', end='')
        for j in range(size-i):
            print('🟧', end='')
        print()
    print()

def main():
    right_triangle(5)
main()

#github.com/tiagodefendi

