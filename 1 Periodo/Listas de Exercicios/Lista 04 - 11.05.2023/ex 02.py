'''
1. Escreva uma função que calcula e devolve o sumtório de um número:
∑𝑖.
Função: def summation(n: int) -> int
OBS: Crie testes para todos os exercícios na função main():
def main():
print(summation(10) == 55) # True
print(summation(5) == 15) # True
print(summation(0) == 0) # True
print(summation(-5) == 0) # True
main() # chamada da função main() para iniciar o programa
--------------------------------------------------------------------------------------------
2. Utilizando a função summation(n) do exercício anterior, escreva uma função que devolve o
produto (multiplicação) dos somatórios de dois números.
Função: def summation_product(a: int, b: int) -> int
'''

def summation(number:int) -> int:
    sum = int()
    for c in range(number+1):
        sum += c
    return sum

def summation_product(number1:int, number2:int):
    return summation(number1) * summation(number2)

def main():
    print(summation_product(5, 3))
    print(summation_product(2, 10))
    print(summation_product(0, 7))
main()

#github.com/tiagodefendi
