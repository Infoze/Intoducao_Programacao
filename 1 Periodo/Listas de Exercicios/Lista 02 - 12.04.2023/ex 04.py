'''
4. Escreva um programa que lê um número de 0 a 9 e o imprime por extenso. O programa deve validar a entrada (0 <= x <= 9) e informar erro, caso ocorra.
'''

numero = int(input('Escolha um valor para o número: '))

if x >= 0 and x <=9:
    if x == 0:
        print(f'O número {numero} escrito por extenso é: Zero')
    if x == 1:
        print(f'O número {numero} escrito por extenso é: Um')
    if x == 2:
        print(f'O número {numero} escrito por extenso é: Dois')
    if x == 3:
        print(f'O número {numero} escrito por extenso é: Três')
    if x == 4:
        print(f'O número {numero} escrito por extenso é: Quatro')
    if x == 5:
        print(f'O número {numero} escrito por extenso é: Cinco')
    if x == 6:
        print(f'O número {numero} escrito por extenso é: Seis')
    if x == 7:
        print(f'O número {numero} escrito por extenso é: Sete')
    if x == 8:
        print(f'O número {numero} escrito por extenso é: Oito')
    if x == 9:
        print(f'O número {numero} escrito por extenso é: Nove')
else:
    print(f'ERRO! O número {numero} não está no intervalo [0, 9]')
    
#github.com/tiagodefendi
