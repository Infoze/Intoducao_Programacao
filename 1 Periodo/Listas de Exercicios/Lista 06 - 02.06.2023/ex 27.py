'''
 27.  Escreva  uma  função  que  recebe  uma  lista  contendo  números  inteiros.  A  função  deve  determinar  o
 segmento de soma máxima, iniciando na posição 0. Ao final, deve imprimir a soma máxima.
 def max_sum_slice(v: list)
 Exemplo: Na lista [  5, 2,-2,-7, 3,14,10,-3, 9  ,-6, 4, 1], a soma máxima é 31
'''

def max_sum_slice(v: list):

    '''sum = 0
    for e in v:
        sum += e
    print(sum)'''

def main():
    max_sum_slice([5, 2,-2,-7, 3,14,10,-3, 9 ,-6, 4, 1])

if __name__ == '__main__':
    main()
