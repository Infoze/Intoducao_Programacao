'''
1. Escreva um programa que lê um número inteiro e informa:
a. Caractere na tabela ASCII (%c);
b. Valor decimal (%d);
c. Valor octal (%o);
d. Valor hexadecimal (%X).
'''

numero = int(input('Escolha um valor para o número: '))

print(f'O valor de {numero} na tabela ASCII é igual a {ord(numero)}')
print(f'O valor de {numero} em Valor Decimal é igual a {numero} ')
print(f'O valor de {numero} em OctalASCII é igual a {oct(numero)}')
print(f'O valor de {numero} em ASCII é igual a {hex(numero)}')
#github.com/tiagodefendi
