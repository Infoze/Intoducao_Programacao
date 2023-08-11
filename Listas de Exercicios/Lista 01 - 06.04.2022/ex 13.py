'''
13. Modifique o programa anterior, letra (b), para que seja possível informar os 3 pesos, além dos 3
valores.

12. Escreva um programa que lê três números inteiros (a, b e c) e informa:
a. A média aritmética simples dos três valores.
b. A média ponderada dos três valores, considerando como pesos 10% (a), 50% (b) e 40% (c).
'''

numero1 = int(input('Escolha um valor para o 1º número:'))
numero2 = int(input('Escolha um valor para o 2º número:'))
numero3 = int(input('Escolha um valor para o 3º número:'))

peso1 = int(input('Escolha um valor para o peso d0 1º número:'))
peso2 = int(input('Escolha um valor para o peso do 2º número:'))
peso3 = int(input('Escolha um valor para o peso do 3º número:'))

mediaSimples = (numero1 + numero2 + numero3)/3
mediaPonderada = (numero1*peso1 + numero2*peso2 + numero3*peso3)/(peso1 + peso2 + peso3)

print(f'O valor da média aritimética entre os valores {numero1}; {numero2}; {numero3}; é equivalente a {mediaSimples}')
print(f'O valor da média ponderada entre os valores {numero1} (Peso {peso1}); {numero2} (Peso {peso2}); {numero3} (Peso {peso3}); é equivalente a {mediaPonderada}')

#github.com/tiagodefendi
