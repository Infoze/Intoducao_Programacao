'''
5. Escreva uma função que calcula e devolve a soma dos fatoriais até um dado número.
∑𝑖!
Você pode escrever uma solução que utiliza 2 laços aninhados (laço dentro de laço).
Função: factorial_sum(n: int) -> int
Exemplo de uso:
print(factorial_sum(5)) # deve calcular 1! + 2! + 3! + 4! + 5! = 153
'''

def factorial_calc(number:int) -> int:
    factorial = 1
    for c in range(1, number+1):
        factorial *= c
    return factorial

def factorial_sum(number:int) -> int:
    sum = int()
    for c in range(1, number+1):
        sum += factorial_calc(c)
    return sum

def main():
    print(factorial_calc(3))
    print(factorial_sum(4))
    print(factorial_sum(5))
main()

#github.com/tiagodefendi
