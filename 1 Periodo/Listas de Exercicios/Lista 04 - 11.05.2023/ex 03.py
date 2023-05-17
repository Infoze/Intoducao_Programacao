'''
3. Escreva uma função que verifica se um dado número é primo. A função deve devolver True, caso o
número seja primo, ou False, caso contrário.
Função: is_prime(x: int) -> bool
'''

def is_prime(number:int) -> bool:
    prime = True
    for c in range(2, number):
        if number % c == 0:
            prime = False
            break
    return prime

def main():
    print(is_prime(7))
    print(is_prime(45))
    print(is_prime(3))
    print(is_prime(6))
main()

#github.com/tiagodefendi
