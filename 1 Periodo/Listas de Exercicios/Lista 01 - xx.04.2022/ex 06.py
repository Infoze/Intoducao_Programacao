'''
6. Escreva um programa que lê o raio (r) de um círculo. O programa deve informar: o diâmetro, a
circunferência e a área do círculo. Considere:
a. pi (π) = 3.141593
b. Diâmetro = 2r
c. Circunferência = 2πr
d. Área = πr²
'''

raio = int(input('Escolha um valor para o raio do seu círculo: '))
pi = 3.141593

diametro = 2 * raio
circuferencia = diametro * pi
area = pi * raio**2

print(f'Um círculo com raio {raio} deve possuir um diâmetro equivalente a {diametro}, sua circunferência será {circuferencia}, e terá uma área de {area}')

#github.com/tiagodefendi
