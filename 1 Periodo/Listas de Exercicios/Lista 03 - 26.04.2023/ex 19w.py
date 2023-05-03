'''
19. Escreva um programa que verifica se um número inteiro é primo, isto é, possui divisão exata
somente pelo próprio número ou por 1. Exemplo:
Informe o número: 67
Resposta: primo
'''

numero = int(input('Escolha um valor para o número: '))
primo = True

contador = 2

while contador < numero:
    if numero % 2 == 0:
        primo = False
        break
    contador += 1

if primo == True:
    print(f'O número {numero} é primo')
else:
    print(f'O numero {numero} não é primo')

#github.com/tiagodefendi
