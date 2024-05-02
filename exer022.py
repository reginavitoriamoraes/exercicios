#Exercício: Faça um programa que leia de 0 á 9999 e mostre na tela cada um dos digitos separados.
#Separando digitos de um número

num=input('Informe um número de 0 a 9999: ')
print(f'Analisando o número {num}')
print(f'unidade: [{num[3:4]}]')
print(f'dezena: [{num[2:3]}]')
print(f'centena: [{num[1:2]}]')
print(f'milhar: [{num[0:1]}]')



