from random import choice

ALUNO_1 = str(input('Primeiro aluno: '))
ALUNO_2 = str(input('Segundo aluno: '))
ALUNO_3 = str(input('Terceiro aluno: '))
ALUNO_4 = str(input('Quarto aluno: '))
lista = [ALUNO_1, ALUNO_2, ALUNO_3, ALUNO_4]
SORTEADO = choice(lista)

print('O aluno escolhido foi ' + SORTEADO)
