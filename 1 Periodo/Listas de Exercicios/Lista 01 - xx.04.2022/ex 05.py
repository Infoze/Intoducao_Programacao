'''
5. Escreva um programa que lê a largura e o comprimento de um retângulo. O programa deve
imprimir o perímetro e a área do retângulo. Considere:
a. Área = largura x comprimento
b. Perímetro = soma de todos os lados
'''

largura = int(input('Escolha um valor para a largura: '))
comprimento = int(input('Escolha um valor para o comprimento: '))

perimetro = 2*largura + 2*comprimento
area = largura * comprimento

print(f'O retângulo {largura} por {comprimento} possui perímetro igual a {perimetro} e área igual {area}')

#github.com/tiagodefendi
