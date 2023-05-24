'''
11. Escreva uma função que converte um número binário (int) para decimal (int). O processo envolve
somar as multiplicações dos dígitos binários por potências de 2, com expoente crescente da direita
para a esquerda. Observe o exemplo:
Função: def bin_to_dec(bin: int) -> int:
100102 = 1x24 + 0x23 + 0x22 + 1x21 + 0x20 = 1810
'''

def bin_to_dec(bin:int) -> int:
    dec = int()
    counter = int()
    while bin % 10 > 0 or bin // 10 > 0:
        dec = dec + ((bin%10)*2)** counter
        bin //= 10
        counter += 1
    return dec

def main():
    print(bin_to_dec(101))
main()

#github.com/tiagodefendi
