'''
7. Escreva um programa que lê dois números inteiros (a e b) e informa:
a. Resto (utilizado o operador %)
b. Resto (sem utilizar o operador %)
i. Dica: Faça a divisão “no papel” e observe quais outras operações podem ser utilizadas para obter o resto.
'''

dividendo = int(input('Escolhar um valor para o dividendo da razão: '))
divisor = int(input('Escolha um valor para o divisor da razão: '))

restoOperador = dividendo % divisor
restoRaiz = (dividendo/divisor - dividendo//divisor)*divisor

print(f'O resto da razão {dividendo}/{divisor} com o operador % é {restoOperador}')
print(f'O resto da razão {dividendo}/{divisor} sem o operador % é {restoRaiz}')

#github.com/tiagodefendi
