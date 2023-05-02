'''
3. Escreva um programa que faz a leitura de um número e exibe os dígitos que o formam, enquanto
for diferente de 0. Dica: use o quociente (divisão inteira) e o resto (%) por 10 para desmontar o
número. O exemplo abaixo demonstra o processo usando as variáveis x (número) e d (dígito).
Observe-o e monte uma solução com laço que permita desmontar números inteiros de qualquer
quantidade de dígitos.
x = 256 | x d
d = x % 10; | 256 6
x = x / 10; | 25 6
d = x % 10; | 25 5
x = x / 10; | 2 5
d = x % 10; | 2 2
x = x / 10; | 0 2 <== laço termina quando x=0
'''

numero = int(input('Escolha um valor para o número: '))
resto = 0

while numero % 10 != 0 or numero // 10 > 0:
    resto = numero  % 10
    numero //= 10
    print(resto)

#github.com/tiagodefendi
