'''
16. Escreva um programa que lê um número de dias e converte em: anos + semanas + dias.
a. Considere:
i. Ano = 365 dias
ii. Semana = 7 dias
Exemplo:
Dias: 427 = 1 ano(s), 8 semana(s) e 6 dia(s)
'''

diasTotal = int(input('Escolha um valor pra o número de dias: '))
anos = diasTotal//365
semanas = (diasTotal%365)//7
diasRestantes = (diasTotal%365)%7

print(f'{diasTotal} dias podem ser divididos em {anos} anos, {semanas} semanas e {diasRestantes} dias')


#github.com/tiagodefendi
