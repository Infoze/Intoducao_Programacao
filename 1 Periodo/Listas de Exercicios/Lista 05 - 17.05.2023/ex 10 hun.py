'''
10. Escreva uma função que exibe um MENU com 5 opções para executar operações. O MENU deve
permitir operar sobre duas variáveis, A e B, que serão lidas por meio das opções [1] e [2]. Dica:
utilize um laço que só termina quando a opção 5 for digitada. Observe o exemplo:
Função: def run_menu()
--------------------------------------------------
SUPREME SUM! A: 0 B: 0 // mostra A e B
--------------------------------------------------
1 - Set A // ler da entrada
2 - Set B // ler da entrada
3 - Show A+B // soma e mostra
4 - Show AxB // multiplica e mostra
5 - Exit
'''

def run_menu():
    option = int()
    a = int()
    b = int()
    while option != 5:
        print(f'''
--------------------------------------------------
SUPREME SUM! A: {a} B: {b}
--------------------------------------------------
1 - Set A
2 - Set B
3 - Show A+B
4 - Show AxB
5 - Exit
              ''')
        option = int(input('Select an option: '))
        if option == 1:
            a = int(input('Set A:'))
        elif option == 2:
            b = int(input('Set B: '))
        elif option == 3:
            print(a+b)
        elif option == 4:
            print(a*b)

def main():
    run_menu()
main()

#github.com/tiagodefendi
