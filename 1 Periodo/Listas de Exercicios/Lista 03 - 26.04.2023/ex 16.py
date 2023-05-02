'''
16. Escreva um programa que exibe a frequência de cada dígito em um número inteiro.
Informe o número: 1251055
> Frequência de 0: 1
> Frequência de 1: 2
> Frequência de 2: 1
> Frequência de 3: 0
> Frequência de 4: 0
> Frequência de 5: 3
> Frequência de 6: 0
> Frequência de 7: 0
> Frequência de 8: 0
> Frequência de 9: 0
'''

numero = int(input('Escolha um valor para o número: '))
resto = 0
frequencia0 = 0
frequencia1 = 0
frequencia2 = 0
frequencia3 = 0
frequencia4 = 0
frequencia5 = 0
frequencia6 = 0
frequencia7 = 0
frequencia8 = 0
frequencia9 = 0

while numero % 10 != 0 or numero // 10 > 0:
    resto = numero  % 10
    numero //= 10
    if resto == 0:
        frequencia0 += 1
    elif resto == 1:
        frequencia1 += 1
    elif resto == 2:
        frequencia2 += 1
    elif resto == 3:
        frequencia3 += 1
    elif resto == 4:
        frequencia4 += 1
    elif resto == 5:
        frequencia5 += 1
    elif resto == 6:
        frequencia6 += 1
    elif resto == 7:
        frequencia7 += 1
    elif resto == 8:
        frequencia8 += 1
    else:
        frequencia9 += 1

print(
    f'''
    frequecia de 0 = {frequencia0}
    frequecia de 1 = {frequencia1}
    frequecia de 2 = {frequencia2}
    frequecia de 3 = {frequencia3}
    frequecia de 4 = {frequencia4}
    frequecia de 5 = {frequencia5}
    frequecia de 6 = {frequencia6}
    frequecia de 7 = {frequencia7}
    frequecia de 8 = {frequencia8}
    frequecia de 9 = {frequencia9}
    '''
)

#github.com/tiagodefendi
