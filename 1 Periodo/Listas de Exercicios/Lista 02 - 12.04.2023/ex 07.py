'''
7. Escreva um programa que faz a leitura de três notas escolares float - n1, n2 e n3 - no intervalo
[0..10]. Após, deve calcular e informar a média aritmética simples das três notas, bem como, o
O aluno obteve o conceito que o aluno obteve com base na média, segundo estes critérios:
a. O aluno obteve o Conceito A, se média no intervalo [8,5..10]
b. O aluno obteve o Conceito B, se média no intervalo [7,0..8,5[
c. O aluno obteve o Conceito C, se média no intervalo [5,5..7,0[
d. O aluno obteve o Conceito F, se média no intervalo [0..5,5[
'''

nota1 = float(input('Escolha um valor para a 1ª nota: '))
nota2 = float(input('Escolha um valor para a 2ª nota: '))
nota3 = float(input('Escolha um valor para a 3ª nota: '))

media = (nota1 + nota2 + nota3)/3

if (nota1 >= 0 and nota1 <=10) and (nota2 >= 0 and nota2 <=10) and (nota3 >= 0 and nota3 <=10):
    if media >= 0 and media < 5.5:
        print(f'O aluno obteve o CONCEITO F! A média entre as notas {nota1}; {nota2}; {nota3} é {media}')
    elif media >= 5.5 and media < 7:
        print(f'O aluno obteve o CONCEITO C! A média entre as notas {nota1}; {nota2}; {nota3} é {media}')
    elif media >= 7 and media < 8.5:
        print(f'O aluno obteve o CONCEITO B! A média entre as notas {nota1}; {nota2}; {nota3} é {media}')
    else:
        print(f'O aluno obteve o CONCEITO A! A média entre as notas {nota1}; {nota2}; {nota3} é {media}')
else:
    print(f'ERRO! As notas devem estar no intervalo de [0, 10]: {nota1}; {nota2}; {nota3}')

#github.com/tiagodefendi
