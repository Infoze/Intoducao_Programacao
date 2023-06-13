'''
18.  Escreva   uma   função   que   recebe   um   valor   inteiro   value   e   uma   lista   notes   com  as  possíveis
 cédulas. A função deve imprimir a quantidade mínima de cédulas equivalente ao valor.
 Dica: use uma lista auxiliar  count  para armazenar a contagem de cada cédula.
 def min_bills(value: int, notes: list)
 Exemplo:   min_bills(209, [1,5,10,50,100])   # lista de tipos de cédulas
 # Saída:
 # 2 x $100
 # 1 x $5
 # 4 x $
'''

def min_bills(value:int, notes:list):
    idx = -1
    counter = 0
    while value > 0:
        if value - notes[idx] >= 0:
            value -= notes[idx]
            counter += 1
        else:
            print(f'{counter} X {notes[idx]}$')
            idx -= 1
            counter = 0
    print(f'{counter} X {notes[idx]}$')


def main():
    notes = [1,2,5,10,20,50,100,200]
    min_bills(5229, notes)

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
