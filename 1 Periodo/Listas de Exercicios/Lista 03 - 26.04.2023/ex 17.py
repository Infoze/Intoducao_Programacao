'''
17. Escreva um programa que verifica se um número inteiro é um palíndromo, isto é, se representa o
mesmo valor quando invertido. Note que será necessário desmontar o número e remontá-lo
invertido. Para tanto, lembre-se de que utilizamos a base 10, o que torna possível “mover” um
número para esquerda multiplicando-o por 10.
Exemplos:
Informe o número: 24742
> 24742 = 24742
> Palíndromo!
Informe o número: 1752
> 1752 != 2571
> Não é palíndromo!
'''

numero = int(input('Escolha um valor para o número: '))

memoria = numero
resto = 0
palindromo = 0

while memoria % 10 != 0 or memoria // 10 > 0:
    resto = memoria  % 10
    memoria //= 10
    palindromo = palindromo * 10 + resto

if numero == palindromo:
    print(f'O número {numero} é um palíndromo')
else:
    print(f'Os números {numero}; {palindromo} não são palíndromos')

#github.com/tiagodefendi
