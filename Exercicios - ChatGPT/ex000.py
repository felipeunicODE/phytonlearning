import math, time

cores = {'':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[36m'}

#Pintura com eficência
alt = float(input('Qual a altura parede: '))
larg = float(input('Qual a largura da parede: '))
latas = int(input('Quantos litros de tinta você possui: '))
area = larg * alt
tinta = area / 2

print(f'A parede tem área total de {area}m² e serão necessários {tinta:.0f} litros para pintar a parede.')


#Unidade e dezena
n = int(input('Digite um número: '))
print(f'{cores['roxo']}ANALISANDO O NÚMERO {cores['amarelo']}{n}{cores['']}')
time.sleep(2)
print(f'A milhar é: {n // 1000 % 10}\nA centena é: {n // 100 % 10}\nA dezena é: {n // 10 % 10}\nA unidade é {n // 1 % 10 }')


#Quebrando um número
#Leia um número real e mostre sua parte inteira e a parte decima.
#6.75 > 6 > 0.75

nr = float(input('Digite um número: '))
#decimal =
print(f'A parte inteira do número {nr} é {int(nr)}.')
print(f'A parte decimal do número {nr} é {'decimal'}')

#Conversor de temperatura
celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15
c = (fahrenheit - 32) / 1.8
print(f'A temperatura em Celsius: {celsius}ºC\nConvertida para Fahrenheit: {fahrenheit}ºF \nConvertida para Kelvin: {kelvin}K')
print(f'A temperatura Fahrenheit convertida para Celsius é: {c}ºC')

#Alugel de carros
dias = int(input('Coloque quantos dias o carro ficou alugado: '))
km = float(input('Quantos km o carro rodou: '))
custo = dias * 60 + km * 0.15
#R$60 * dia
#R$0.15 * km
print(f'Total a pagar pelo carro: R${custo:.2f}')

#Desconto progressivo
print(f'{cores['ciano']}-='*20)
print(f'{cores['azul']:^13}GERENTE FICOU MALUCO')
print(f'{cores['ciano']}-='*20)
print(f'{cores['amarelo']}Até R$100 - 5% de desconto{cores['']}\n{cores['roxo']}Mais de R$100 - 10% de desconto{cores['']}')
p = float(input('Qual o valor do produto: ')) #100
print(f'{cores['roxo']}APLICANDO DESCONTO...{cores['']}')

time.sleep(2)

if p <=100:
    print(f'O produto com valor de {cores['amarelo']}R${p:.2f}{cores['']} com {cores['amarelo']}5%{cores['']} de desconto ficou {cores['verde']}R${p - (p * 0.5):.2f}{cores['']}')
else:
    print(f'O produto com valor de {cores['roxo']}R${p:.2f}{cores['']} com {cores['roxo']}10%{cores['']} de desconto ficou {cores['verde']}R${p - (p * 0.10):.2f}{cores['']}')

#Nome completo - Análise
print(f'{cores['amarelo']}='*30)
print(f'{cores['roxo']:^9}VAMOS ANALISAR SEU NOME')
print(f'{cores['amarelo']}={cores['']}'*30)
nome = str(input('Qual o seu nome: ').strip())
print(f'{cores['roxo']}FAZENDO ANÁLISE...{cores['']}')
time.sleep(2)
print(f'{cores['verde']}ANÁLISE CONCLUIDA:{cores['']}')
print(f'Seu nome TODO MAIUSCULO: {nome.upper()}')
print(f'Seu nome TODO MINUSCULO: {nome.lower()}')
print(f'Quantidade de LETRAS no seu nome: {len(nome.replace(' ',''))}')
print(f'Seu primeiro nome tem {len(nome.split()[0])} letras')


