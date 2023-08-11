'''
10. Escreva um programa que lê um valor em graus e o converte para radianos. Considere:
a. pi = 3.141593 ⇒ 180 graus
'''

numeroGraus = int(input('Escolha um valor em graus para ser convertido em radianos: '))
pi = 3.141593

numeroRadiano = numeroGraus * pi / 180

print(f'{numeroGraus}° é equivalente a {numeroRadiano} radianos')

#github.com/tiagodefendi
