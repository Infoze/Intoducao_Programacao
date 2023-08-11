'''
20. A série de Fibonacci é 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Os dois primeiros termos são iguais a 1 e, a
partir do terceiro, o termo é dado pela soma dos dois termos anteriores. Dado um número n≥3,
exiba o n-ésimo termo da série de Fibonacci.
'''

limite = int(input('Escolha um valor para o limite: '))

numero1 = 1
numero2 = 0
memoria = 0

contador = 1

while contador <= limite:
    memoria = numero2
    numero2 = numero1 + numero2
    numero1 = memoria
    contador += 1

print(f'O valor do {limite}º termo na sequencia de fibonacci é {numero2}')

#github.com/tiagodefendi
