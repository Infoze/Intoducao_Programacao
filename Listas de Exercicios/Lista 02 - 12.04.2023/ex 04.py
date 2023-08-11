'''
4. Escreva um programa que lê um número de 0 a 9 e o imprime por extenso. O programa deve validar a entrada (0 <= x <= 9) e informar erro, caso ocorra.
'''

numero = int(input('Escolha um valor para o número: '))

if numero < 0 or numero >9:
    print(f'ERRO! O número {numero} não está no intervalo [0, 9]')
else:
    if numero == 0:
        print(f'O número {numero} escrito por extenso é: Zero')
    elif numero == 1:
        print(f'O número {numero} escrito por extenso é: Um')
    elif numero == 2:
        print(f'O número {numero} escrito por extenso é: Dois')
    elif numero == 3:
        print(f'O número {numero} escrito por extenso é: Três')
    elif numero == 4:
        print(f'O número {numero} escrito por extenso é: Quatro')
    elif numero == 5:
        print(f'O número {numero} escrito por extenso é: Cinco')
    elif numero == 6:
        print(f'O número {numero} escrito por extenso é: Seis')
    elif numero == 7:
        print(f'O número {numero} escrito por extenso é: Sete')
    elif numero == 8:
        print(f'O número {numero} escrito por extenso é: Oito')
    elif numero == 9:
        print(f'O número {numero} escrito por extenso é: Nove')
    
#github.com/tiagodefendi
