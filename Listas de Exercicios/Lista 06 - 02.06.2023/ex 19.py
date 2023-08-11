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
'''

def histogram(days:list):
    for e in days:
        if e < 0:
            e *= -1
        print('>'*e)

def main():
    histogram([5,8,12,11,10,7,-1])

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
