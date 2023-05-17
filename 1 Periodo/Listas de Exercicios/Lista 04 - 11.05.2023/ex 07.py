'''
7. Escreva uma função que imprime N números inteiros aleatórios. A função receberá como
parâmetro a quantidade de números (n) e os limites para sorteio (min e max). Os números devem
ser randomizados entre [min, max]. Utilize a semente 1 antes de gerar os números, isto é,
random.seed(1).
OBS: Será necessário utilizar a função random.randint() do módulo random. Para tanto, importe o
módulo random com import random.
Função: print_random(n: int, min: int, max: int)
Exemplos de testes:
print_random(5, -10, 10) # saída: -6 8 -8 -2 -7
print_random(20, 0, 1) # saída: 0 0 1 0 1 1 1 1 0 0 1 0 1 1 0 1 1 0 0 1
'''

from random import seed, randint

def print_random(number:int, min:int, max:int):
    seed(1)
    for c in range(number):
        print(randint(min, max), end=' ')
    print()

def main():
    print_random(5, -10, 10)
    print_random(20, 0, 1)
    print_random(8, 0, 1)
    print_random(1, 1, 14)
main()

#github.com/tiagodefendi
