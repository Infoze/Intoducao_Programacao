'''
13.  Escreva  uma  função  que  recebe  uma  lista  vet  e  devolve  seus  3  maiores  elementos.  Obs:  Não  é
 permitido o uso de max() e list.sort()
 def get_max3(vet: list) -> tuple[int, int, int
'''

def get_max3(vet:list) -> tuple[int, int]:
    st_higher = -float("inf")
    nd_higher = -float("inf")
    rd_higher = -float("inf")
    for e in vet:
        if e > st_higher:
            rd_higher = nd_higher
            nd_higher = st_higher
            st_higher = e
        elif e > nd_higher and e < st_higher:
            rd_higher =  nd_higher
            nd_higher = e
        elif e > rd_higher and e < nd_higher:
            rd_higher = e
    return st_higher, nd_higher, rd_higher

def main():
    print(get_max3([5,3,7,8,4,9]))
    print(get_max3([10,9,8,45,3]))

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
