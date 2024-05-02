print('Aluguel de carros')
days=int(input('Quantos dias alugados? '))
km=float(input('Quantos KM rodados? '))
amounttopay= days * 60.00
amounttopaykm= km * 0.15
valortotal= amounttopay + amounttopaykm
print(f'O valor do aluguel por dia é de : {amounttopay} e o valor que percorreu é de R$ {amounttopaykm} sendo assim o valor total a pagar é de {valortotal}')


#dia R#60,00
#km rodado 0.15