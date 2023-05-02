'''
18. O quadrado de um número natural n é dado pela soma dos n primeiros números ímpares
consecutivos. Por exemplo, 1²=1, 2²=1+3, 3²=1+3+5, 4²=1+3+5+7, etc. Dado um número n, calcule
seu quadrado usando a soma de ímpares.
'''

numero = int(input('Escolha um valor para saber seu quadrado: '))
quadrado = 0

for impar in range(1, numero*2):
    if impar % 2 == 1:
        quadrado += impar

print(quadrado)

#github.com/tiagodefendi
