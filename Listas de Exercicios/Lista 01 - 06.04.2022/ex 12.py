'''
12. Escreva um programa que lê três números inteiros (a, b e c) e informa:
a. A média aritmética simples dos três valores.
b. A média ponderada dos três valores, considerando como pesos 10% (a), 50% (b) e 40% (c).
'''

numero1 = int(input('Escolha um valor para o 1º número:'))
numero2 = int(input('Escolha um valor para o 2º número:'))
numero3 = int(input('Escolha um valor para o 3º número:'))

mediaSimples = (numero1 + numero2 + numero3)/3
mediaPonderada = numero1*0.1 + numero2*0.5 + numero3*0.4

print(f'O valor da média aritimética entre os valores {numero1}; {numero2}; {numero3} é equivalente a {mediaSimples}')
print(f'O valor da média ponderada entre os valores {numero1} (Peso 1); {numero2} (Peso 5); {numero3} (Peso 4) é equivalente a {mediaPonderada}')

#github.com/tiagodefendi
