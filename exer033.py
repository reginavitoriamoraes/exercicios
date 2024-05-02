salario = float(input('Qual o seu salario atual? R$'))
if salario > 1250.00:
    aumento = 10 * salario / 100
    novo_salario = aumento + salario
else: 
    aumento = 15 * salario / 100
    novo_salario = aumento + salario
print(f'Com o novo aumento, seu salário passou a ser R${novo_salario}')



