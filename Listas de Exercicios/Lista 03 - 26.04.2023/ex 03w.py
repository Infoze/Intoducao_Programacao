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

contador = 1

while contador <= 10:
    print(f'{numero} X {contador : >2} = {numero * contador : >2}')
    contador += 1

#github.com/tiagodefendi
