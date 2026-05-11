#Tabuada
n = int(input('Coloque um número: ')) # 5
print('Este é o resultado da tabuada do ', n)
print('-'*13)
print('{} x {:2} = {}'.format(n, 1, n*1))
print('{} x {:2} = {}'.format(n, 2, n*2))
print('{} x {:2} = {}'.format(n, 3, n*3))
print('{} x {:2} = {}'.format(n, 4, n*4))
print('{} x {:2} = {}'.format(n, 5, n*5))
print('{} x {:2} = {}'.format(n, 6, n*6))
print('{} x {:2} = {}'.format(n, 7, n*7))
print('{} x {:2} = {}'.format(n, 8, n*8))
print('{} x {:2} = {}'.format(n, 9, n*9))
print('{} x {:2} = {}'.format(n, 10, n*10))
print('-'*13)

#Conversor de Moedas
r = float(input('Coloque quantos reais você tem na carteira: R$')) #cotação US$4,94 E$5.81
d = r / 4.94
eu = r / 5.81
print('Com {:.2f} reais você pode comprar: \n{:.2f} dolares \n{:.2f} euros'.format(r, d, eu))