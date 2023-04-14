'''
12. Escreva uma versão modificada do programa anterior, agora informando se o caractere é uma letra, 
independente do mesmo ser informado como minúscula ou maiúscula.
'''

letra = str(input('Escolha caractere para a variável: '))
letraNumero = ord(letra)


if (letraNumero >= 65 and letraNumero <= 90) or (letraNumero >= 97 and letraNumero >= 122):
    print(f'O caractere "{letra}" é uma letra')
else:
    print(f'O caractere "{letra}" não é uma letra')

#github.com/tiagodefendi
