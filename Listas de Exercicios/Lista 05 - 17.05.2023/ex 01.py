'''
1. Escreva uma função que imprime a tabuada completa, de 1 a 10. Pense em uma solução que se
beneficia do uso de laços aninhados.
Função: def mult_table()
'''

def mult_table():
    print('-------------')
    for i in range(1, 11):
        for j in range(1, 11):
            print(f'{i: >2} X {j: >2} = {(i*j): >2}')
        print('-------------')

def main():
    mult_table()
main()

#github.com/tiagodefendi
