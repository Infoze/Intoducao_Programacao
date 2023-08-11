'''
9. Escreva um programa que imprime a tabuada de um número informado, em duas colunas.
Ex: Informe o número: 5
TABUADA DO NÚMERO 5
5 x 1 = 5 5 x 6 = 30
5 x 2 = 10 5 x 7 = 35
5 x 3 = 15 5 x 8 = 40
5 x 4 = 20 5 x 9 = 45
5 x 5 = 25 5 x 10= 50
'''

numero = int(input('Escolha um valor para se imprimir a tabuada: '))

print(f'''
-------------------------
   Tabuada do número {numero}
-------------------------''')

print(f'{numero} X 1  = {numero*1 : >2}   {numero} X 6  = {numero*6 : >2}')
print(f'{numero} X 2  = {numero*2 : >2}   {numero} X 7  = {numero*7 : >2}')
print(f'{numero} X 3  = {numero*3 : >2}   {numero} X 8  = {numero*8 : >2}')
print(f'{numero} X 4  = {numero*4 : >2}   {numero} X 9  = {numero*9 : >2}')
print(f'{numero} X 5  = {numero*5 : >2}   {numero} X 10 = {numero*10 : >2}')

#github.com/tiagodefendi
