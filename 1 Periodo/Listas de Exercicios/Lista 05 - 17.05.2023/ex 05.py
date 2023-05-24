'''
5. Dados dois parâmetros naturais m e n, escreva uma função que exibe um retângulo formado por
caracteres "X" intercalados com "-", tendo n caracteres "X" de largura. As linhas devem estar
contidas entre colchetes.
Função: def xbox(m: int, n: int)
Exemplo: m=3 e n=6
[X-X-X-X-X-X]
[X-X-X-X-X-X]
[X-X-X-X-X-X]
'''

def xbox(height:int, width:int):
    for i in range(height):
        print('[', end='')
        for j in range(width*2-1):
            if j % 2 == 0:
                print('X', end='')
            else:
                print('-', end='')
        print(']')
    print()

def main():
    xbox(3,3)
    xbox(3, 6)
main()

#github.com/tiagodefendi

