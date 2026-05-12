import math, time, random

cores = {'':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[36m'}

#Sorteio simples
n1 = str(input('Nome um: '))
n2 = str(input('Nome dois: '))
n3 = str(input('Nome três: '))
n4 = str(input('Nome quatro: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(f'A lista embaralhada foi: {(lista)}')
print(f'O nome sorteado é: {(lista[0])}')

#O shuffle embaralha a lista, mostra pro usuário e o primeiro nome é selecionado
#Estava utilizando o shuffle para embaralhar a lista e o choice para captar um nome dentre os 4, o que não estava fazendo lógica já que estava embaralhando um, mostrando a ordem e o nome escolhido era outro

#Pintura com eficência
    #1 litro cobre 2m²
    #quantas latas de 5 litros serão necessárias?

alt = float(input('Qual a altura parede: '))
larg = float(input('Qual a largura da parede: '))

area = larg * alt
tinta = area / 2
latas = math.ceil(tinta / 5) #uma lata de tinta possui 5 litros e a cad 1 litro se pinta 2m
#O cálculo é a quantidade de litros / por 1 lata que possui 5 litros
print(f'A parede tem área total de {area}m² e serão necessários {tinta:.0f} litros de tinta para pintar a parede. Devem ser compradas {latas} latas de tinta.')
#não entendi a questão das latas


#Quebrando um número
#Leia um número real e mostre sua parte inteira e a parte decima.
#6.75 > 6 > 0.75

nr = float(input('Digite um número: '))
print(f'A parte inteira do número {nr} é {int(nr)}.')
print(f'A parte decimal do número {nr} é {nr - int(nr)}')

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
    print(f'O produto com valor de {cores['amarelo']}R${p:.2f}{cores['']} com {cores['amarelo']}5%{cores['']} de desconto ficou {cores['verde']}R${p - (p * 0.05):.2f}{cores['']}')
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

#Unidade e dezena
n = int(input('Digite um número: '))
print(f'{cores['roxo']}ANALISANDO O NÚMERO {cores['amarelo']}{n}{cores['']}')
time.sleep(2)
print(f'A milhar é: {n // 1000 % 10}\nA centena é: {n // 100 % 10}\nA dezena é: {n // 10 % 10}\nA unidade é {n // 1 % 10 }')


#Conversor de dinheiro de IOF
r = float(input('Coloque o valor em reais: '))
d = r / 4.91
iof = d + (d * 0.0638)

print(f'O valor de R${r:.2f} convertido em dollar sem imposto é U${d:.2f}.\nCom IOF de 6.38% sobre {d:.2f}: U${iof:.2f}')

#Analise de número inteiro
n = int(input('Digite um número: '))

if n % 2 == 0:
    print(f'O número {n} é IMPAR')
else:
    print(f'O número {n} é PAR')
if n == 0:
    print(f'O número digitado foi: {n}')
if n >= 0:
    print('Número positivo')
else:
    print('Número negativo')
#não entendi como se faz pra verificar se o numero eh negativo ou positivo

#Reajuste inteligente
s = float(input('Informe o salário do funcionário: R$'))
if s <= 1250:
    print(f'O salário de R${s:.2f} com aumento de 15% foi para: R${s + (s * 0.15):.2f}')
else:
    print(f'O salário de R${s:.2f} com aumento de 10% foi para: R${s + (s * 0.10):.2f}')

#Distância entre dois pontos
print('Para calcular a distância entre o ponto A e o ponto B, preencha:')
x1 = float(input('Digite o número para x1: ')) #1
y1 = float(input('Digite o número para y1: ')) #2
x2 = float(input('Digite o número para x2: ')) #4
y2 = float(input('Digite o número para y2: ')) #6
print(f'O ponto A = {x1}, {y1}')
print(f'O ponto B = {x2}, {y2}')
a = x2 - x1
b = y2 - y1
d = math.sqrt((a) ** 2 + (b) ** 2)
print(f'A distância entre o ponto A e B é: {d:.2f}')

#Desafio Bônus
print('Olá, tudo bem? Me informe alguns dados para analisarmos.')
nome = str(input('Me fale seu nome completo: ')).strip()
idade = int(input('Quantos anos você possui? '))
salario = float(input('Me informe seu salário R$'))
print(f'{cores['roxo']}ANALISANDO....{cores['']}')
time.sleep(2)
print(f'{cores['amarelo']}GERANDO RELATÓRIO....{cores['']}')
time.sleep(5)
print(f'{cores['verde']}ANÁLISE CONCLUIDA')
print(f'Seu nome em MAIUSCULO: {nome.upper()}')
print(f'Sua idade em dias (aproximado): {idade * 365}')
print(f'Se houvesse um aumento salarial de 10% seu salário seria: {salario + (salario * 0.1):.2f}{cores['']}')
