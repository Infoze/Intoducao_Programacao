'''
14. Escreva um programa que lê um caractere e informa:
a. Se é letra e, neste caso, também informa se é vogal ou consoante;
b. Se é número;
c. Se é símbolo (ASCII 33 ao 126, exceto números e símbolos).
'''

caractere = str(input('Escolha caractere para a variável: '))
caractereNumero = ord(caractere)

if (caractereNumero >= 65 and caractereNumero <= 90) or (caractereNumero >= 97 and caractereNumero <= 122):
    if caractereNumero == 65 or caractereNumero == 69 or caractereNumero == 73 or caractereNumero == 79 or caractereNumero == 85 or caractereNumero == 97 or caractereNumero == 101 or caractereNumero == 105 or caractereNumero == 111 or caractereNumero == 117:
        print(f'O caractere "{caractere}" é uma vogal')
    else:
        print(f'O caractere "{caractere}" é uma consoante')
elif caractereNumero >= 48 and caractereNumero <= 57:
    print(f'O caractere "{caractere}" é um número')
else:
    print(f'O caractere "{caractere}" é um símbolo na tabela ASCII')

#github.com/tiagodefendi
