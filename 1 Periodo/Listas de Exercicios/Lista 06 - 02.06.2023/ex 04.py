'''
 4.   Escreva uma função que recebe uma lista  vet  e devolve a média aritmética simples dos elementos.
 def list_sum(vet: list) -> float
 Ex: Entrada: [1, 23, 4, 8, 41, 7, 3] → Saída: 12
'''

def list_sum(vet: list) -> float:
    sum = int()
    for e in vet:
        sum += e
    return sum/len(vet)

def main():
    print(list_sum([1, 2, 3]))
    print(list_sum([10, 8, 8, 3.5]))

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
