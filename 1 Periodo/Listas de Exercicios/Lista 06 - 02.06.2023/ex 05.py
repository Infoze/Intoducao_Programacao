'''
 5.   Escreva  uma  função  que  recebe  uma  lista  vet  ,  bem  como,  um  elemento  elem  a  ser  procurado.  A
 função deve retornar a posição (índice) do elemento ou  None  caso ele não esteja no vetor.
 def find(vet: list, elem: int)
'''

def find(vet: list, elem: int):
    for i in range(len(vet)):
        if vet[i] == elem:
            return i
    raise ValueError

def main():
    print(find([2,4,5,6,5,3], 8))

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
