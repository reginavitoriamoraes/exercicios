print('Seja bem vindo pintor!!')
larg= float(input(f'Informe a largura da sua parede: '))
alt= float(input(f'Informe a altura da sua parede: '))
area= larg * alt
print(f'Sua parede tem a dimensão de {larg} x {alt} e sua área é {area}²')
tinta = area / 2
print(f'Para pintar a sua parede você irá precisar de {tinta}l de tinta.')