'''
4. Escreva um programa que lê dois números inteiros (a e b) e informa:
a. Multiplicação
b. Divisão inteira (a dividido por b)
c. Divisão real
'''

numero1 = int(input('Escolha um valor para o 1º número: '))
numero2 = int(input('Escolha um valor para o 2º número: '))

multiplicacao = numero1 * numero2
divisaoInteira = numero1 // numero2
divisaoReal = numero1 / numero2

print(f'A multiplicação entre {numero1} e {numero2} resulta em {multiplicacao}')
print(f'A divisão inteira entre {numero1} e {numero2} resulta em {divisaoInteira}')
print(f'A divisão real entre {numero1} e {numero2} resulta em {divisaoReal}')

#github.com/tiagodefendi
