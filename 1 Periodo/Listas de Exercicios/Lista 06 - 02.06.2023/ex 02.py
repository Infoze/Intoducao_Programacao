'''
 2.   Escreva uma função que recebe uma lista  vet  e imprime apenas os valores pares.
 def print_even(vet: list)
'''

def print_even(vet: list):
    for e in vet:
        if e % 2 == 0:
            print(e, end='; ')
    print('\b\b ')

def main():
    print_even([2,3,4,6,67,78,100])

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
