'''
 9.   Escreva   uma   função  que  verifica  se  os  elementos  de  uma  lista  estão  em  ordem  crescente.  A
 função  deve  retornar  True,  caso  os  elementos  estejam  dispostos  em  ordem  crescente,  ou  False,
 em caso contrário. Obs:  Não é permitido o uso de list.sort()  .
 def  is_sorted(vet: list) -> bool
 Exemplo de uso da função:   v = [1,4,7,9,15,22,48,512]
 print(is_sorted(v)) # Tru
'''

def is_sorted(vet:list) -> bool:
    memory = vet[0]
    for e in vet:
        if memory > e:
            return False
        memory = e
    return True

def main():
    print(is_sorted([1,2,3,4,5,7,89,100]))
    print(is_sorted([1,2,6,4,5,7,89,100]))


if __name__ == '__main__':
    main()

#github.com/tiagodefendi
