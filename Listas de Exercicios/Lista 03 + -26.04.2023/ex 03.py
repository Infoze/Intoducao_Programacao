'''
4. Escreva um programa que, dado um número inteiro (positivo ou negativo) entre -999 e 999, o
imprime por extenso. Caso o número esteja fora desse intervalo, o programa deve informar um
erro.
Informe o número: 572
> quinhentos e setenta e dois (positivo)
'''

numero = int(input('Escolha um valor para o número: '))

contador = 1

unidade = 0
dezena = 0

#while
memoria = numero

#Negativo
negativo = False

if memoria < 0:
    memoria = -memoria
    negativo = True

#while
while memoria % 10 > 0 or memoria // 10 > 0:
    if contador == 1:
        unidade = memoria % 10
    if contador == 2:
        dezena = memoria % 10
    memoria //= 10
    contador += 1

#print
if contador <= 3:
    print(f'O número {numero} por extenso é: ', end='')

    #dezena
    if dezena == 1:
        if unidade == 0:
            print('dez', end='')
        elif unidade == 1:
            print('onze', end='')
        elif unidade == 2:
            print('doze', end='')
        elif dezena == 3:
            print('treze', end='')
        elif dezena == 4:
            print('quatorze', end='')
        elif dezena == 5:
            print('quinze', end='')
        elif dezena == 6:
            print('dezesseis', end='')
        elif dezena == 7:
            print('dezessete', end='')
        elif dezena == 8:
            print('dezoito', end='')
        elif dezena == 9:
            print('dezenove', end='')
    elif dezena == 2:
        print('vinte', end='')
    elif dezena == 3:
        print('trinta', end='')
    elif dezena == 4:
        print('quarenta', end='')
    elif dezena == 5:
        print('cinquenta', end='')
    elif dezena == 6:
        print('sessenta', end='')
    elif dezena == 7:
        print('setenta', end='')
    elif dezena == 8:
        print('oitenta', end='')
    elif dezena == 9:
        print('noventa', end='')

    if (unidade != 0) and dezena !=0:
        print(' e ', end='')

    #unidade
    if unidade == 1:
        print('um', end=' ')
    elif unidade == 2:
        print('dois', end=' ')
    elif unidade == 3:
        print('três', end=' ')
    elif unidade == 4:
        print('quatro', end=' ')
    elif unidade == 5:
        print('cinco', end=' ')
    elif unidade == 6:
        print('seis', end=' ')
    elif unidade == 7:
        print('sete', end=' ')
    elif unidade == 8:
        print('oito', end=' ')
    elif unidade == 9:
        print('nove', end=' ')

    #negativo
    if negativo == True:
        print('(negativo)')
    else:
        print('(positivo)')
else:
    if numero > 99:
        print(f'EROO! O número {numero} é maior que 99')
    else:
        print(f'ERRO! O número {numero} é menor que -99')

#github.com/tiagodefendi

