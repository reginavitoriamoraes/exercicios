#Conversor de medidas
print('seja bem vindo ao meu conversor de medidas!')
metro=float(input('Digite o valor em metros: '))
cm= round(metro * 100, 2)
mm= round(metro * 1000, 2)
print(f'{metro} metros equivale a {cm} centímetros')
print(f'{metro} metros equivale a {mm} milímetros')