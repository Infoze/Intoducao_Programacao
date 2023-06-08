'''
 26.  Escreva  uma  função  que  recebe  duas  listas  v1  e  v2,  ordenadas  crescentemente.  A  função  deve
 mesclar   ordenadamente   os   conteúdos   de   v1   e   v2  ,   colocando-os   em   uma   nova   lista,   a   ser
 retornada. OBS:  não é permitido o uso de list.sort() e do operador +  .
 def list_merge(v1: list, v2: list)
 Entrada:   v1 = [1, 3, 4, 7, 9, 10]
 v2 = [2, 3, 5, 7, 7, 14]
 Saída:   v3 = [1, 2, 3, 3, 4, 5, 7, 7, 7, 9, 10, 14]
'''

def list_merge(v1:list, v2:list):
    v3 = []
    i = 0
    j = 0
    while i < len(v1) and j < len(v2):
        if v1[i] < v2[j]:
            v3.append(v1[i])
            i += 1
        else:
            v3.append(v2[j])
            j += 1
    while i < len(v1):
        v3.append(v1[i])
        i += 1
    while j < len(v2):
        v3.append(v2[j])
    return v3

def main():
    v1 = [1,2,6,7,88]
    v2 = [2,3,4,5,8,9]
    print(list_merge(v1, v2))

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
