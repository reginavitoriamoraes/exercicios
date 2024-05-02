#Maior e menor valores 


v1=int(input('Digite o primeiro valor: '))
v2=int(input('Digite o segundo valor: '))
v3= (input('Digite o terceiro valor: '))

if v1<v3 and v1<v2:
    print(f'O menor valor é {v1}')
if v2<v1 and v2<v3:
    print(f'O menor valor é {v2}')
if v3<v1 and v3<v2:
    print(f'O menor valor é {v3}')


if v1>v2 and v1>v3:
    print(f'O maior valor é {v1}')
if v2>v1 and v2>v3:
    print(f'O maior valor é {v2}')
if v3>v2 and v3>v1:
    print(f'O maior valor é {v3}')
