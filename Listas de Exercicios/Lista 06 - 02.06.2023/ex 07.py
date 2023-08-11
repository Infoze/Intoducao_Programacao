'''
7.   Escreva  uma  função  que  recebe  uma  lista  vet  e  um  número  value  .  A  função  deve  retornar  uma
 outra lista, contendo os múltiplos de  value  que estão em  vet  .
 def get_multiples(vet: list, value: int) -> list
'''

def get_multiples(vet: list, value: int) -> list:
    list = []
    for e in vet:
        if e % value == 0:
            list.append(e)
    return list

def main():
    print([1,2,3,6,7,8,10,4], get_multiples([1,2,3,6,7,8,10,4], 2))

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
