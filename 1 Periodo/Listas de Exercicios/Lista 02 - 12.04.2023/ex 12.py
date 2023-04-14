'''
12. Escreva uma versão modificada do programa anterior, agora informando se o caractere é uma letra, 
independente do mesmo ser informado como minúscula ou maiúscula.
'''

caractere = str(input('Escolha caractere para a variável: '))
caractereNumero = ord(caractere)

if (caractereNumero >= 65 and caractereNumero <= 90) or (caractereNumero >= 97 and caractereNumero <= 122):
    print(f'O caractere "{caractere}" é uma letra')
else:
    print(f'O caractere "{caractere}" não é uma letra')

#github.com/tiagodefendi
