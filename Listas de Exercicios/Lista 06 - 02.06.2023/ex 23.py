'''
 23.  Escreva  uma  função  que  recebe  duas  listas  e  realiza  a  interseção  entre  o  conteúdo  de  ambas,
 colocando o resultado em uma nova lista, a ser retornada.
 def list_intersection(v1: list, v2: list) -> list
 Exemplo:
 v3 = list_intersection([1,2,3,4,5], [8,2,4,9])  # v3 = [2,4]
'''

def list_intersection(v1: list, v2: list) -> list:
    intersection = []

    for i in v1:
        for j in v2:
            if i == j and i not in intersection:
                intersection.append(i)

    return intersection

def main():
    v1 = [1,2,3,4,3,2,3,7,8]
    v2 = [2,3,8,9,10]
    print(list_intersection(v1, v2))

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
