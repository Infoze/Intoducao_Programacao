'''
 1.   Escreva  uma  função  que  recebe  uma  lista  vet  a  imprime  em  ordem  reversa.  Não  é  permitido  o  uso
 de list.reverse()  .
 def print_reverse(vet: list
'''

def print_reverse(vet: list):
    for i in range(-1, -1 -len(vet), -1):
        print(vet[i], end='; ')
    print('\b\b ')

def main():
    print_reverse([1,2,4,7,0,9])

if __name__ == '__main__':
    main()
