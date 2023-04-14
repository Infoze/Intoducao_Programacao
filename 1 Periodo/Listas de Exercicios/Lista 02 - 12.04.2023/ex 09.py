'''
9. Escreva um programa que lê três números e os escreve em ordem crescente.
'''

numero1 = int(input('Escolha um valor para o 1º número: '))
numero2 = int(input('Escolha um valor para o 2º número: '))
numero3 = int(input('Escolha um valor para o 3º número: '))

if (numero1 >= numero2) and (numero2 >= numero3): #1 > 2 > 3
    print(f'A sequência em ordem crescente dos valores [{numero1, numero2, numero3}] é {numero1} >= {numero2} >= {numero3}')
    
if (numero1 >= numero3) and (numero3 >= numero2):#1 > 3 > 2
    print(f'A sequência em ordem crescente dos valores [{numero1, numero2, numero3}] é {numero1} >= {numero3} >= {numero2}')
    
if (numero2 >= numero1) and (numero1 >= numero3):#2 > 1 > 3
    print(f'A sequência em ordem crescente dos valores [{numero1, numero2, numero3}] é {numero2} >= {numero1} >= {numero3}')
    
if (numero2 >= numero3) and (numero3 >= numero1):#2 > 3 >1
    print(f'A sequência em ordem crescente dos valores [{numero1, numero2, numero3}] é {numero2} >= {numero3} >= {numero1}')
    
if (numero3 >= numero1) and (numero1 >= numero2):#3 > 1 > 2
    print(f'A sequência em ordem crescente dos valores [{numero1, numero2, numero3}] é {numero3} >= {numero1} >= {numero2}')
    
if (numero3 >= numero2) and (numero2 >= numero1):#3 > 2 > 1
    print(f'A sequência em ordem crescente dos valores [{numero1, numero2, numero3}] é {numero3} >= {numero2} >= {numero1}')

#github.com/tiagodefendi
