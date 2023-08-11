'''
3. Escreva uma função que verifica se um dado número é primo. A função deve devolver True, caso o
número seja primo, ou False, caso contrário.
Função: is_prime(x: int) -> bool
---------------------------------------------------------------------------------------------
4. Utilizando a função is_prime(x) do exercício anterior, escreva uma função que imprime os n
primeiros números primos.
Função: print_primes(n: int)
'''

def is_prime(number:int) -> bool:
    prime = True
    for c in range(2, number):
        if number % c == 0:
            prime = False
            break
    return prime

def print_prime(number: int):
    counter = 2
    primes = 0
    while primes < number:
        if is_prime(counter) == True:
            print(counter, end=' ')
            primes += 1
        counter +=1
    print()

def main():
    print_prime(6)
    print_prime(8)
main()

#github.com/tiagodefendi
