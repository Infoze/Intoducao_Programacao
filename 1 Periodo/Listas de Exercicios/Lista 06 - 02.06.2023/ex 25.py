'''
25.  Escreva  uma  função  que  recebe  duas  listas  de  inteiros  (  bin1  e  bin2  )  de  mesmo  tamanho,  que
 devem  ser  interpretadas  como  dois  números  binários  de  n  algarismos.  A  função  deve  calcular  a
 sequência  de  números  que  representa  a  soma  dos  dois  binários,  colocando-a  em  uma  nova  lista  a
 ser retornada.
 def binary_sum(bin1: list, bin2: list)
 carry   1    1    1    1    1    1    0    0    0
 bin1:   1    1    0    0    1    1    0    1
 bin2:   +    0    1    1    1    0    1    1    0
 -------------------------------------------
 return:   1    0    1    0    0    0    0    1
'''

def binary_sum(bin1: list, bin2: list):
    carry = 0
    sum = []
    for i in range(-1, -(len(bin1)+1), -1):
        if bin1[i] + bin2[i] + carry == 0:
            carry = 0
            sum.insert(0, 0)
        elif bin1[i] + bin2[i] + carry == 1:
            carry = 0
            sum.insert(0, 1)
        elif bin1[i] + bin2[i] + carry == 2:
            carry = 1
            sum.insert(0, 0)
        elif bin1[i] + bin2[i] + carry == 3:
            carry = 1
            sum.insert(0, 1)

    print(sum)

def main():
    bin1 = [0,0,1]
    bin2 = [1,0,1]
    binary_sum(bin1, bin2)

    bin1 = [0,0,1,0,0,1]
    bin2 = [1,0,1,0,0,1]
    binary_sum(bin1, bin2)

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
