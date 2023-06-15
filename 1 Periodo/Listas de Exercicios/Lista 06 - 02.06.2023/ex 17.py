'''
17.  Escreva  uma  função  que  recebe  uma  lista  vet  preenchido  com  inteiros  positivos.  A  função  deve
 imprimir  as  ocorrências  (contagem)  de  cada  número  na  lista.  Dica:  utilize  uma  lista  count  para
 armazenar  a  contagem  de  cada  elemento  na  lista  vet  ,  relacionando  as  posições  de  count  aos
 valores  em  vet  . A lista count precisa ter tamanho max(vet)+1.
 def count_elements(vet: list)
'''

def count_elements(vet:list):
    vet.sort()
    elements = []
    count = []
    for i in range(len(vet)):
        counter = 0

        if i == 0 or vet[i] != elements[-1]:
            elements.append(vet[i])

            for j in vet:
                if elements[-1] == j:
                    counter += 1

            count.append(counter)

    return count


def main():
    list = [1,2,3,4,4,5,4,3,6,7,3]
    print(count_elements(list))


if __name__ == '__main__':
    main()

#github.com/tiagodefendi
