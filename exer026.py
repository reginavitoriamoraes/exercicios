#Jogo de advinhação 


from random import randint
print('Jogo de advinhação ')
print('-=-'*30)
print('Tente vencer a máquina..')
print('Vou pensar em um número entre 0 e 5, tente advinhar...')
num1= int(input('Em que número pensei?? '))
computador= randint (0,5) 
if num1 == computador:
    print('parabéns, você me venceu!!!!')
else:
    print('Não foi dessa vez!!!')
print(f'Pensei no número {computador}')
print('-=-'*30)
num2= int(input('Em que número pensei?? '))
computador1= randint (0,5) 
if num2 == 1:
    print('parabéns, você me venceu!!!!')
else:
    print('Não foi dessa vez!!!')
print(f'Pensei no número {computador1}')
print('-=-'*30)
num3= int(input('Em que número pensei?? '))
computador2= randint (0,5) 
if num3 == 1:
    print('parabéns, você me venceu!!!!')
else:
    print('Não foi dessa vez!!!')
print(f'Pensei no número {computador2}')
print('-=-'*30)
print('FIM...')
    