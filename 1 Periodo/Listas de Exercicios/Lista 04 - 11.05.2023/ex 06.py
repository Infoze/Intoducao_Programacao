'''
5. Escreva uma função que calcula e devolve a soma dos fatoriais até um dado número.
∑𝑖!
Você pode escrever uma solução que utiliza 2 laços aninhados (laço dentro de laço).
Função: factorial_sum(n: int) -> int
Exemplo de uso:
print(factorial_sum(5)) # deve calcular 1! + 2! + 3! + 4! + 5! = 153
--------------------------------------------------------------------------------------------------
6. Escreva uma nova versão da função do exercício anterior, agora utilizando apenas um único laço
para realizar a operação solicitada na função. Dica: observe a representação dos cálculos.
Função: factorial_sum2(n: int) -> int
Exemplo de uso:
print(factorial_sum2(5))
1! + 2! + 3! + 4! + 5! = 153, é o mesmo que:
1! = 1 = 1 +
2! = 1 x 2 = 2 +
3! = 1 x 2 x 3 = 6 +
4! = 1 x 2 x 3 x 4 = 24 +
5! = 1 x 2 x 3 x 4 x 5= 120
                        153
'''

def factorial_sum2(number:int) -> int:
    counter = 1
    factorial = 1
    counter_factorial = 1
    sum = 0
    while counter_factorial <= number:
        if counter <= counter_factorial:
            factorial *= counter
            counter += 1
        else:
            sum += factorial
            counter = 1
            factorial = 1
            counter_factorial += 1
    return sum

def main():
    print(factorial_sum2(5))
main()

#github.com/tiagodefendi
