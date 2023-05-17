'''
1. Escreva uma função que calcula e devolve o somatório de um número:
∑𝑖.
Função: def summation(n: int) -> int
OBS: Crie testes para todos os exercícios na função main():
def main():
print(summation(10) == 55) # True
print(summation(5) == 15) # True
print(summation(0) == 0) # True
print(summation(-5) == 0) # True
main() # chamada da função main() para iniciar o programa
'''

def summation(number:int) -> int:
    sum = int()
    for c in range(number+1):
        sum += c
    return sum

def main():
    print(summation(10) == 55)
    print(summation(5) == 15)
    print(summation(0) == 0)
    print(summation(-5) == 0)
    print(summation(5) == 10)

main()

#github.com/tiagodefendi
