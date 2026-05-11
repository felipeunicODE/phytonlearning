#Largura x Altura
lg = float(input('Largura da parede: '))
al = float(input('Altura da parede: '))
area = lg * al
tinta = area / 2
print('Sua parede tem uma dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}m².'.format(lg, al, area))
print('Para pintar esta parede, você precisara de {:.2f}l de tinta.'.format(tinta)) #a cada 1l de tinta pinta-se 2m²

#Desconto
produto = float(input('Coloque o valor do produto: R$'))
desc = 5 / 100
aplicado = produto * desc
valor = produto - aplicado
print ('O produto que custava R${:.2f}, com o desconto de 5% irá custar R${:.2f}.'.format(produto, valor))

#Aumento
sal = float(input('Coloque o salário do colaborador: R$'))
aumento = sal + (sal * 15 / 100)
print('O salário do colaborador que era R${:.2f} com o aumento de 15% foi para R${:.2f}'.format(sal, aumento))