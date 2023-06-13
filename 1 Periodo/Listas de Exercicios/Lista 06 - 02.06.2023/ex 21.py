'''
 21.  Escreva  uma  função  que  recebe  duas  listas  e  concatena  o  conteúdo  de  ambas  em  uma  nova  lista,
 a ser retornada. Obs:  Não é permitido o uso de list.extend() e do operador +  .
 def list_concat(v1: list, v2: list) -> list
 Exemplo:
 list = list_concat([1,2,3,4], [5,6,7])   # list = [1,2,3,4,5,6,7
'''

def list_concat(v1:list, v2:list) -> list:
    list = v1.copy()
    list.extend(v2.copy())
    return list

def main():
    print(list_concat([1,2,3],[6,7,8]))

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
