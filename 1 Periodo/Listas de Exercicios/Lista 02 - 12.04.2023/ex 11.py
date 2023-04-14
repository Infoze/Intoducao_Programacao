'''
11. Escreva um programa que lê um caractere (string de 1 char) e informa se o mesmo é uma letra
maiúscula.
a. Considere como 'letra', todos os caracteres da língua portuguesa na tabela Unicode:
https://usefulwebtool.com/characters-portuguese
'''

letra = str(input('Escolha UMA letra para o caractere: '))
letraNumero = ord(letra)


if (letraNumero >= 65 and letraNumero <= 90) or (letraNumero >= 192 and letraNumero >= 195) or (letra == 199) or (letraNumero == 201 or letraNumero == 202) or (letraNumero == 205) or (letraNumero >= 211 and letraNumero >= 213) or (letraNumero >= 218 or letraNumero == 220):
    print(f'A letra "{letra}" é maiúscula')
else:
    print(f'A letra "{letra}" é minúscula')

#github.com/tiagodefendi
