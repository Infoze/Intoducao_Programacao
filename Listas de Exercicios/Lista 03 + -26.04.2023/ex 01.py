'''
1. Escreva um programa que, dado um número inteiro (positivo ou negativo), troca o último dígito pelo
primeiro. OBS: não basta imprimir o número dessa forma, é preciso inverter o número em uma
variável int.
Informe o número: -2567
> -7562
'''

numero = int(input('Escolha um valor para o número: '))

memoria = numero
contrario = 0
negativo = False

if memoria < 0:
    memoria = -memoria
    negativo = True

while memoria % 10 > 0 or memoria // 10 > 0:
    contrario = contrario*10 + memoria % 10
    memoria //= 10

if negativo == True:
    memoria = -memoria

print(f'O contrario do valor {numero} é {contrario}')

#github.com/tiagodefendi
