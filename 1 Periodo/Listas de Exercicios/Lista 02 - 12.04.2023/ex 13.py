'''
13. Escreva um programa que lê um caractere da entrada. Se não for letra, informa. Se for letra,
verifica se é maiúscula (e passa para maiúscula se necessário). Ao final, deve informar a letra
digitada em maiúsculo.
'''

caractere = str(input('Escolha caractere para a variável: '))
caractereNumero = ord(caractere)

if (caractereNumero >= 65 and caractereNumero <= 90) or (caractereNumero >= 97 and caractereNumero <= 122):
    if:
        print(f'O caractere "{caractere}" é uma letra')
    if:
        print
    
else:
    print(f'O caractere "{caractere}" não é uma letra')

#github.com/tiagodefendi
