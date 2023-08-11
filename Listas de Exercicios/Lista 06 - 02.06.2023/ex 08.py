'''
 8.   Escreva uma função que recebe uma lista  vet  e retorna uma outra lista, com os primos em vet.
 def get_primes(vet: list) -> list
'''

def get_primes(vet: list) -> list:
    primes = []
    for e in vet:
        is_prime = True
        if e == 1 or e == 0:
            is_prime = False
        for i in range(2, e):
            if e % i == 0:
                is_prime = False
        if is_prime == True:
            primes.append(e)
    return primes


def main():
    print(get_primes([0, 1,2,3,4,5,6,7,10,11,13,45,47,49]))

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
