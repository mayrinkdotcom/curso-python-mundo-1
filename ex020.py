from random import shuffle

ALUNO1 = str(input('Primeiro aluno: '))
ALUNO2 = str(input('Segundo aluno: '))
ALUNO3 = str(input('Terceiro aluno: '))
ALUNO4 = str(input('Quarto aluno: '))
lista = [ALUNO1, ALUNO2, ALUNO3, ALUNO4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)
