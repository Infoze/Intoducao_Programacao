'''
6. Escreva um programa que, dado um número inteiro positivo, imprime seus fatores primos.
Informe o numero:
> 132
2 x fator 2
1 x fator 3
1 x fator 11
'''

numero = int(input('Escolha um valor para o número: '))

memoria = numero
primo = 2
contador = 0

print(f'Os fatores primos de {numero} são:')

while primo <= numero:
    if memoria % primo == 0:
        memoria /= primo
        contador += 1

    else:
        if contador >= 1:
            print(f'{contador} X fator {primo}')
        primo += 1
        contador = 0



#github.com/tiagodefendi
