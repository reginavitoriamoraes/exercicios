print('seja bem vindo ao programa de custo da viagem!!')
distancia=float(input('Qual a distância da viagem em km?'))
if distancia <=200:
    valor=distancia * 0.50
else: 
    valor=distancia * 0.45
print(f'o valor da viagem é R${valor} ')