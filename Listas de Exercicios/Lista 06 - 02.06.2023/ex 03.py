'''
 3.   Escreva  uma  função  que  recebe  uma  lista  vet  contendo  números  inteiros.  A  função  deve  modificar
 a lista, invertendo o sinal dos números negativos, passando-os para positivo.
 def set_positive(vet: list)
 Ex: Entrada:[1, -5, 67, -45, -1, -1, 0, 48] → Saída:[1, 5, 67, 45, 1, 1, 0, 48]
'''

def set_positive(vet: list):
    for i in range(len(vet)):
        if vet[i] < 0:
            vet[i] *= -1
    return vet

def main():
    vet = [1, 3,56,-67, 4, -9, -10]
    print(vet)
    print(set_positive(vet))

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
