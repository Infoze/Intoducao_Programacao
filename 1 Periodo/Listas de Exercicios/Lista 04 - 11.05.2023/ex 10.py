'''
10. Escreva uma função que imprime uma sequência de n números randômicos entre [left, right]
(inclusivos). Ao final, a função deve devolver o maior e o menor números sorteados.
Função: print_random2(n: int, left: int, right: int) -> tuple[int, int]
Exemplo de uso:
# imprime 50 números entre -500 e 500. Devolve o maior e o menor.
min,max = print_random2(50, -500, 500)
print(f'min: {min}, max: {max}')
'''

from random import randint as rd

def print_random2(number:int, left:int, right:int) -> tuple[int, int]:

    random = rd(left, right)
    maior = random
    menor = random
    print(random, end=' ')
    for c in range(1, number):

        random = rd(left, right)
        print(random, end=' ')
        if random > maior:
            maior = random
        elif random < menor:
            menor = random
    print()
    print(f'Maior: {maior}')
    print(f'Menor: {menor}')

def main():
    print_random2(3, 1, 10)
    print_random2(6, 5, 25)
    print_random2(50, -500, 500)
main()

#github.com/tiagodefendi
