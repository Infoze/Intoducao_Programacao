'''
3. Escreva um programa que imprime a tabuada de um número informado. Exemplo:
Informe o número: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
...
7 x 10 = 70
'''

numero = int(input('Escolha um valor para a tabuada: '))

for multiplicador in range(1, 11):
    print(f'{numero} X {multiplicador : >2} = {numero*multiplicador : >2}')

#github.com/tiagodefendi
