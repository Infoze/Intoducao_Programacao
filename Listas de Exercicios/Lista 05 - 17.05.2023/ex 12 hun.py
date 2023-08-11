'''
12. Escreva uma função que imprime um tablado de tamanho 20x10, contendo um personagem "#", que
deverá ser controlado pela entrada dos caracteres WASD. O personagem inicia no centro do
trabalho - posição (10, 10). O código deve controlar a posição (linha x coluna) do personagem e
alterá-la conforme os caracteres WASD forem informados. Note que, ao imprimir o tablado, é
necessário considerar a posição em que se encontra o personagem para imprimí-lo na posição
adequada. O código deve impedir que o personagem seja movido além dos limites do tablado. De
forma geral, o programa consiste em:

1. Ler caractere do teclado (W-A-S-D ou Q);
a. Cada um dos caracteres WASD corresponde à uma direção;
b. O caractere Q (“quit”) deve encerrar o programa.

2. De acordo com o caractere informado (WASD), deve alterar (adicionar/subtrair) a
linha/coluna correspondente, de forma a reposicionar o personagem;
a. W: linha -= 1, S: linha += 1, A: coluna -= 1, D: coluna += 1

3. Reimprimir o tablado após cada entrada, conforme exemplo abaixo. Considerar a posição
em que deve ser impresso o caractere do personagem ("#").
MOVE-A-MOVE             MOVE-A-MOVE
╔═══════════════════╗   ╔═══════════════════╗   ╔═══════════════════╗
║                   ║   ║                   ║   ║                   ║
║                   ║   ║                   ║   ║            #      ║
║                   ║   ║                   ║   ║                   ║
║         #         ║   ║            #      ║   ║                   ║
║                   ║   ║                   ║   ║                   ║
║                   ║   ║                   ║   ║                   ║
║                   ║   ║                   ║   ║                   ║
║                   ║   ║                   ║   ║                   ║
╚═══════════════════╝   ╚═══════════════════╝   ╚═══════════════════╝
Teclas: A⇦W⇧D⇨S⇩       Teclas: A⇦W⇧D⇨S⇩       Teclas: A⇦W⇧D⇨S⇩
> W (enter)             > DDD (enter)            > WW (enter)
(move p/ cima)          (move 3x p/ direita)     (move 2x p/ cima)

Função: def move_a_move(m: int)
'''

def print_line(number:int, fill:str, edge:str, edge2:str, char:str, char_locate:int):
    for c in range(number):
        if c == 0:
            print(f'{edge}', end='')
        elif c == (number-1):
            print(f'{edge2}', end='')
        elif c == char_locate:
            print(f'{char}', end='')
        else:
            print(f'{fill}', end='')
    print()

def move_a_move():
    quit = ''
    char = ''
    height = 5
    width = 10
    while quit != 'Q':
        print_box(height, width)
        char = input('> ').upper()
        for c in char:
            print(c)
            if c == 'W' and height - 1 != 0:
                height -= 1
            elif c == 'S' and height + 1 != 9:
                height += 1
            if c == 'D' and width + 1 != 19:
                width += 1
            elif c == 'A' and width - 1 != 0:
                width -= 1

            if c == 'Q':
                quit = 'Q'

def print_box(height:int , widht:int):
    for i in range(10):
        if i == 0:
            print_line(20, '═', '╔', '╗', '', 0)
        elif i == 9:
            print_line(20, '═', '╚', '╝', '', 0)
        elif i == height:
            print_line(20, ' ', '║', '║', '#', widht)
        else:
            print_line(20, ' ', '║', '║', '', 0)

def main():
    move_a_move()

if __name__ == '__main__':
    main()


#github.com/tiagodefendi
