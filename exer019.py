#Sorteando um item na lista
from random import choice

aluno1=str(input('Informe seu nome: '))
aluno2=str(input('Informe seu nome: '))
aluno3=str(input('Informe seu nome: '))
aluno4=str(input('informe seu nome: '))
lista= [aluno1, aluno2, aluno3, aluno4]
escolhido= random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')


