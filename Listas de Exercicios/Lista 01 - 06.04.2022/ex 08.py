'''
8. Escreva um programa que imprime a tabuada de um número informado, em uma coluna.
Ex: Informe o número: 5
TABUADA DO NÚMERO 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10= 50
Você pode alinhar os valores na saída com %2d (dois dígitos, alinhados à direita) com o operador
% (módulo string). Também é possível alinhar usando f-string. Veja exemplos no código:
# Imprimindo valores alinhados usando % e f-string
num = 2
print("Alinhado 5 casas à direita.: %5d" % (num)) # % (módulo string)
print("Preenchido com zeros.......: %05d" % (num))
print(f"Alinhado 5 casas à esquerda...: {num : <5}") # f-string
print(f"Alinhado 5 casas à direita....: {num : >5}")
print(f"Alinhado 5 casas centralizado.: {num : ^5}")
Referência para o operador %:
https://realpython.com/python-modulo-string-formatting/#use-the-modulo-operator-for-string-formatting-in-python
'''

numero = int(input('Escolha um valor se imprimir a tabuada: '))

print(f'''
------------
Tabuada do {numero}
------------''')

print(f'{numero} X 1  = {numero*1 : >2}')
print(f'{numero} X 2  = {numero*2 : >2}')
print(f'{numero} X 3  = {numero*3 : >2}')
print(f'{numero} X 4  = {numero*4 : >2}')
print(f'{numero} X 5  = {numero*5 : >2}')
print(f'{numero} X 6  = {numero*6 : >2}')
print(f'{numero} X 7  = {numero*7 : >2}')
print(f'{numero} X 8  = {numero*8 : >2}')
print(f'{numero} X 9  = {numero*9 : >2}')
print(f'{numero} X 10 = {numero*10 : >2}')

#github.com/tiagodefendi
