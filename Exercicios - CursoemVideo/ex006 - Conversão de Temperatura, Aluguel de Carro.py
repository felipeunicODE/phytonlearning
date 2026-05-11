c = float(input('Qual a temperatura em graus Celsius? '))
f = c * 1.8 + 32
print('A temperatura {}°C convertida para Fahrenheit é {:.1f}°F'.format(c, f))

d = int(input('Qual a quantidade de dias o carro foi alugado? '))
km = float(input('Qual a quantidade km percorrido? '))
total = d * 60 + km * 0.15

print(f'O valor total a ser pago pelo carro é de {total:.2f} reais.')
