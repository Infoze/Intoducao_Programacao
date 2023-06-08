'''
 16.  Escreva  uma  função  que  recebe  uma  lista  vet  e  inverte  os  seus  elementos  na  própria  lista.  Obs:
 Não é permitido o uso de list.reverse()  .
 def reverse_list(vet: list
'''

def reverse_list(vet:list):
    for i in range(1,len(vet)//2):
        vet[i], vet[-(i+1)] = vet[-(i+1)], vet[1]


def main():
    vet = [1,2,3,4]
    print(vet)
    reverse_list(vet)
    print(vet)


if __name__ == '__main__':
    main()

#github.com/tiagodefendi
