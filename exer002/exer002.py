#Dissecando uma váriável
a=input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(a))
print('só tem espaços', a.isspace())
print('é um número?', a.isnumeric())
print('é alfanúmerico? ', a.isalnum())
print('está em maiusculas?', a.isupper())
print('Está em minusculas? ', a.islower())
print('Está capitalizada?', a.istitle())


#Todos os is:
#alfabetico - isalpha 
#numerico - isnumeric
#só tem espaços - isspace
#alfabético e numérico - isalnum
#está em maiúsculas - isupper
#está em minúculas - islower
#está só com a primeira letra em maiúsulas - istitle