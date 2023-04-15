'''
15. Escreva uma calculadora simples: faz a leitura de um operador char (+ - * / %), bem como, os
valores inteiros A e B. Então, o programa deve mostrar a expressão e o resultado (com dois dígitos
de precisão).
Exemplo:
[ CALCULADORA SIMPLEX ]
Operador> /
Número01> 20
Número02> 3
Expressão:
20 / 3 = 6.67
'''

operacao = input('Escolha a operação para a calculadora realizar: ')
numero1 = int(input('Escolha um valor para o 1º número: '))
numero2 = int(input('Escolha um valor para o 2º número: '))

if operacao == '+':
    print(f'O resultado de {numero1} {operacao} {numero2} = {numero1 + numero2}')
elif operacao == '-':
    print(f'O resultado de {numero1} {operacao} {numero2} = {numero1 - numero2}')
elif operacao == '*':
    print(f'O resultado de {numero1} {operacao} {numero2} = {numero1 * numero2}')
elif operacao == '/':
    print(f'O resultado de {numero1} {operacao} {numero2} = {numero1 / numero2}')
elif operacao == '%':
    print(f'O resultado de {numero1} {operacao} {numero2} = {numero1 % numero2}')
elif operacao == '//':
    print(f'O resultado de {numero1} {operacao} {numero2} = {numero1 // numero2}')
elif operacao == '**':
    print(f'O resultado de {numero1} {operacao} {numero2} = {numero1 ** numero2}')


#github.com/tiagodefendi
