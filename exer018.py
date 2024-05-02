import math

print('Cateto e Hipotenusa')
catetoposto= float(input('Comprimento do cateto oposto:'))
catetoadjascente= float(input('Comprimento do cateto adjascente:'))
hipotenusa= (catetoposto ** 2 + catetoadjascente ** 2) ** (1/2)
print(f'O valor da hipotenusa é {hipotenusa}')



print('utilizando a biblioteca')
catetoposto= float(input('Comprimento do cateto oposto:'))
catetoadjascente= float(input('Comprimento do cateto adjascente:'))
hipotenusa= math.hypot (catetoposto, catetoadjascente)
print(f'A hipotenusa vai medir {hipotenusa}')
