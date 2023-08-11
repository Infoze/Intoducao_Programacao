'''
9. Escreva um programa que, dado um número inteiro positivo, o imprime em notação binária. O
processo de obtenção é similar à extrair os dígitos de um número: divisões sucessivas por 2, até
que o quociente seja 0 (zero). A cada divisão, o resto indica um dígito binário. Entretanto, assim
como no algoritmo de obter os dígitos, os dígitos binários estarão em ordem inversa. Logo, será
preciso remontar o número binário (na ordem correta) em uma variável inteira. Observe o exemplo:
25 (decimal) = 11001 (binário)
'''

numero = int(input('Escolha um valor para o número: '))

memoria = numero
binarioContrario = 0

while memoria // 2 > 0:
    binarioContrario = binarioContrario * 10 + memoria % 2
    memoria //= 2
binarioContrario = binarioContrario * 10 + memoria % 2

binario = 0

while binarioContrario % 10 > 0 or binarioContrario // 10 > 0:
    binario = binario * 10 + binarioContrario % 10
    binarioContrario //= 10

print(f'O número {numero} em binário é {binario}')

#github.com/tiagodefendi
