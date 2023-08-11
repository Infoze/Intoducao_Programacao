'''
8. Escreva uma função que imprime um Triângulo de Floyd de m linhas. Observe o padrão numérico:
Função: def floyd(m: int)
Para m=6:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
'''

def floyd(size):
    counter = 1
    for i in range(1, size+1):
        for j in range(i):
            print(counter, end=' ')
            counter += 1
        print()

def main():
    floyd(6)
main()

#github.com/tiagodefendi

