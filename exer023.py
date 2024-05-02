#Verificando as primeiras letras de um texto

cid=str(input('Em qual cidade vc nasceu?')).strip()
print(cid[0:5].upper() in 'SANTOS')