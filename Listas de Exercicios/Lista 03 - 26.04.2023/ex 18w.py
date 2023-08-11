'''
18. O quadrado de um número natural n é dado pela soma dos n primeiros números ímpares
consecutivos. Por exemplo, 1²=1, 2²=1+3, 3²=1+3+5, 4²=1+3+5+7, etc. Dado um número n, calcule
seu quadrado usando a soma de ímpares.
'''

numero = int(input('Escolha um valor para saber seu quadrado: '))

quadrado = 0
contador = 1
impar = 1

while contador <= numero:
    quadrado += impar
    impar += 2
    contador += 1

print(f'O quadrado do número {numero} é {quadrado}')

#github.com/tiagodefendi
