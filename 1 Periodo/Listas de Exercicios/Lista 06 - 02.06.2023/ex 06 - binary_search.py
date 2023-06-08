'''
6.   Escreva  uma  função  que  recebe  uma  lista  vet  ordenado  crescentemente,  bem  como,  um  elemento
 elem  a  ser  procurado.  A  função  deve  retornar  a  posição  (índice)  do  elemento  ou  None  caso  ele
 não  esteja  na  lista.  OBS:  Tente  usar  o  fato  da  lista  estar  ordenada  para  criar  uma  solução
 melhor que a anterior
 def find(vet: list, elem: int)
'''

def find(vet: list, elem: int):
    first = 0
    last = len(vet) - 1
    while first <= last:
        m = (first + last)//2
        if vet[m] == elem:
            return m
        if vet[m] > elem:
            last = m - 1
        if vet[m] < elem:
            first = m + 1
    return None

def main():
    print(find([1,2,4,4,6,8,9,43,44,67,100], 6))
    print(find([1,2,4,4,6,8,9,43,44,67,100], 101))

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
