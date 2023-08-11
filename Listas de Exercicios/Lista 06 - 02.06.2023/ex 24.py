'''
 24.  Escreva  uma  função  para  imprimir  o  número  de  acertos  de  cada  aluno  em  uma  prova.  A  prova
 possui 20 questões e cada questão tem cinco alternativas (A, B, C, D, E). Para isso são dados:
 a.   lista  check  , de 20 elementos, com o gabarito;
 b.   lista  answers,  com  as  respostas  dos  alunos,  contendo  as  20  respostas  de  cada  aluno,  em
 sequência.
 i.   A  lista  contém  as  respostas  de  todos  os  alunos  (20  para  cada  aluno).  Dessa  forma,  o
 tamanho da lista é múltiplo de 20. Se forem 10 alunos,  answers  terá tamanho 200.
 def check_tests(check: list, answers: list
'''

def check_tests(check: list, answers:list):
    score = 0
    students = len(answers) // len(check)
    for i in range(0, len(answers), students):
        for j in range(0, students):
            if check[j] == answers[i+j]:
                score += 1
        print(f'Student {i//students+1}: {score}')
        score = 0

def main():
    check = ['A','B','B']
    answers = ['A','B','B','C','D','B','B','B','B']
    check_tests(check, answers)

if __name__ == '__main__':
    main()

#github.com/tiagodefendi
