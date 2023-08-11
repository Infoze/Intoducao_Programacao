'''
 19.  Escreva   uma   função   que   recebe   uma   lista   days   de   tamanho   7  que  exibe  um  histograma  da
 variação  da  temperatura  durante  a  semana.  A  lista  days  armazena  as  temperaturas  para  cada  dia
 da  semana,  iniciando  por  domingo  .  Por  exemplo,  se  as  temperaturas  em  days  forem  [19,  21,  25,
 22, 20, 17 e 15] graus celsius, a função deverá exibir:
 D: >>>>>>>>>>>>>>>>>>>
 S: >>>>>>>>>>>>>>>>>>>>>
 T: >>>>>>>>>>>>>>>>>>>>>>>>>
 Q: >>>>>>>>>>>>>>>>>>>>>>
 Q: >>>>>>>>>>>>>>>>>>>>
 S: >>>>>>>>>>>>>>>>>
 S: >>>>>>>>>>>>>>>
 def histogram(days: list)
--------------------------------------------------------------------------------------------------------------
 20.  Chamando  a  função  desenvolvida  no  exercício  anterior,  escreva  uma  função  que  recebe  a  lista
 days  e exibe:
 a)   As temperaturas média, mínima, máxima;
 b)   O histograma.
 def temperature_report(days: list)
'''

def histogram(days:list):
    for e in days:
        if e < 0:
            e *= -1
        print('>'*e)

def temperature_report(days:list):
    higher = -float("inf")
    smaller = float("inf")
    average = 0
    for e in days:
        if e > higher:
            higher = e
        elif e < smaller:
            smaller = e
        average += e
    average /= 7
    print(f'Average:{average:.3}; Max:{higher}; Min:{smaller}')
    histogram(days)



def main():
    temperature_report([5,8,12,11,10,7,-1])

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
