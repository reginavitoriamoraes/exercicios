#Analisador de texto 
fullname=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
firstname=fullname.split()[0] .strip ()
separador = fullname.split()
print(f'Seu nome tem um total de {len(firstname)} letras')
print(f'Seu primeiro nome é {separador[0]} e ele tem {len(separador[0])} letras')

fullname=fullname.lower()
print(f'Seu nome em mínusculas é {fullname} ')

fullname=fullname.upper()
print(f'Seu nome em maísculas é {fullname} ')

fullname=len(fullname)
print(f'A quantidade de caracteres do seu nome completo é de {fullname} letras')

dividido = fullname.find(' ')
primeiro = fullname.split()
print(f'Seu primeiro nome é {primeiro[0]} e tem {dividido} letras')


print(f'Seu primeiro nome tem ao todo {fullname} letras')
