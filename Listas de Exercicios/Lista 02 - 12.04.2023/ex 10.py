'''
10. Escreva um programa que lê um número de 5 dígitos e imprime cada dígito separado. Para
desmontar um número, podemos utilizar a notação posicional, isto é, o valor de cada dígito em
relação a uma potência de 10. Observe o exemplo:
O processo ocorre como uma repetição de dois passos:
a. Calcular o resto da divisão do número por 10 para obtermos o dígito da unidade.
b. Atualizar o número, dividindo-o por 10. Isso fará o número perder um dígito.
n = 23491
n    | n%10 | n/10
23491| 1    | 2349
2349 | 9    | 234
234  | 4    | 23
23   | 3    | 2
2    | 2    | 0
**Atenção**: você não deve converter o número para str. Ele deve ser sempre tratado como int.
'''

numero = int(input('Escolha um valor de 5 dígitos para um número: '))

unidade = numero%10
dezena = numero//10%10
centena = numero//100%10
unidadeMilhar = numero//1000%10
dezenaMilhar = numero//10000%10

print(f'O número {numero} pode ser impresso separadamente como: {dezenaMilhar} - {unidadeMilhar} - {centena} - {dezena} - {unidade}')

#github.com/tiagodefendi
