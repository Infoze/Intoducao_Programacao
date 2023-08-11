
def print_ascii(col):
    for i in range(col):
        print('DEC OCT HEX CHR   ',end='')
    print()

    n = 94//col + 1# qtde de elementos por coluna
    c = 33
    for i in range(n):
        for j in range(col):
            idx = c + n * j
            if idx > 126: 
                break
            print('%03d %03o %03X %2c    ' % (idx,idx,idx,idx), end='')
        print()
        c += 1

def main():
    print('<< TABELA ASCII >>\n')
    cols = int(input('Colunas? '))
    print_ascii(cols)
    print()

main()