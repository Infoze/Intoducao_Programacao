'''
22.  Escreva   uma   função   que   recebe   duas   listas   e   realiza   a   união   entre   o   conteúdo   de   ambas,
 colocando o resultado em uma nova lista, a ser retornada.
 def list_union(v1: list, v2: list) -> list
 Exemplo:
 v3 = list_union([1,2,3,4,5], [8,2,4,9])   # v3 = [1,2,3,4,5,8,9
'''

def list_union(v1:list, v2:list) -> list:
    union = []
    i = 1
    j = 1

    if v1[0] == v2[0]:
        union.append(v1[0])
    elif v1[0] != v2[0]:
        union.extend([v1[0], v2[0]])

    while i < len(v1) and j < len(v2):
        if v1[i] == v2[j] and v1[i] not in union:
            union.append[i]

        elif v1[0] != v2[0]:
            if v1[i] not in union:
                union.append(v1[i])
            if v2[j] not in union:
                union.append(v2[j])

        i += 1
        j += 1

    while i < len(v1):
        if v1[i] not in union:
            union.append(v1[i])
        i += 1
    while j < len(v2):
        if v1[j] not in union:
            union.append(v2[j])
        j += 1

    return union

def main():
    v1 = [1,2,3,4,3,2,3,7,8]
    v2 = [2,3,8,9,10]
    print(list_union(v1, v2))

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
