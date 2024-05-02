#Exercício 25
#Primeira e última ocorrência de uma string

frase=str(input('Digite uma frase: ')).strip().upper()
letra = str(input('Digite uma letra para saber imformaçoes sobre ela na frase: ')).upper().strip()
print('-' * 20)
q = frase.count(letra)
primeira = frase.find(letra) + 1
ultima = frase.rfind(letra) + 1
print(f'Resultados para a letra {letra}:')
print(f'Quantidade: {q}')
print(f'Posição da primeira: {primeira}')
print(f'Posição da última: {ultima}')
print('-' * 20)