#Analisando o triângulo
print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)

reta1=float(input('Primeiro segmento: '))
reta2=float(input('Segundo segmento: '))
reta3=float(input('Terceiro segmento: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Os segmentos acima podem formar um triânngulo')
else: 
    print('Os segmentos acima não formam um triângulo')


#if reta1 != reta2 != reta3:
   # escaleno= print(f'Forma um triângulo escaleno')
if reta1 == reta2 == reta3:
    equilatero= print(f'Forma um triângulo equilatero')
if reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
    isosceles= print(f'Forma um triangulo isosceles')

