'''
14. Escreva um programa que lê um número float (com parte decimal) e informa separadamente:
a. O número com 2 casas de precisão ("%.2f");
b. A parte inteira;
c. A parte decimal;
'''

numero = float(input('Escolha um valor com casas decimais para um número: '))

parteInteira = numero // 1
parteDecimal = numero - parteInteira

print(f'O número {numero:.2f} tem sua parte inteira equivalente a {parteInteira}: sua parte decimal é igual a {parteDecimal:.2f}')

#github.com/tiagodefendi
