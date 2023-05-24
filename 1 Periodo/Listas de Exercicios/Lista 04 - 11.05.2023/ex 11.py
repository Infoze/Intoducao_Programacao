'''
11. Escreva uma função que imprime uma sequência de n números randômicos entre [left, right]
(inclusivos). Ao final, a função deve devolver a contagem de pares e primos. Considere 0 (zero)
como par. OBS: utilize a função is_prime(x) do exercício 3 para simplificar a verificação de número
primo.
Função: rand_report(n: int, left: int, right: int) -> tuple[int, int]
Exemplo de uso:
# imprime 50 números entre -500 e 500. Devolve contagem de pares e
primos
even,prime = rand_report(50, -500, 500)
print(f'total: {n}, even: {even}, odd: {n-even}, primes: {prime}')
'''
from random import randint as rd

def is_prime(number:int) -> bool:
    prime_anal = True
    if number != 1 or number != 0:
        for c in range(2, number):
            if number % c == 0:
                prime_anal = False
                break
    else:
        prime_anal = False
    return prime_anal

def is_pair(number:int)-> bool:
    pair_anal = True
    if number %2 == 1:
        pair_anal = False
    return pair_anal

def rand_report(number:int, left:int, right:int) -> tuple[int, int]:
    pair_counter = int()
    prime_counter = int()
    for c in range(number):
        random = rd(left, right)
        print(random, end=' ')
        if is_pair(random) == True:
            pair_counter += 1
        if is_prime(random) == True:
            prime_counter += 1
    print()
    return pair_counter, prime_counter

def main():
    pairs, primes = rand_report(5, 0, 6)
    print(f'pairs: {pairs}, primes:{primes}')

    pairs, primes = rand_report(10, 4, 5)
    print(f'pairs: {pairs}, primes:{primes}')

    pairs, primes = rand_report(50, -500, 500)
    print(f'pairs: {pairs}, primes:{primes}')

main()

#github.com/tiagodefendi
