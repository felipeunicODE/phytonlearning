import random, math, time, datetime

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[36m'}

#Adivinhação
print(f'{cores['ciano']}=-{cores['limpa']}'*28)
print(f'{cores['azul']}Vou pensar em um número entre 0 e 5, tente adivinhar...{cores['limpa']}')
print(f'{cores['ciano']}=-{cores['limpa']}'*28)
n = random.randint(0,5) #Faz o computador "PENSAR"
u = int(input(f'{cores['azul']}Em que número eu pensei? ')) #Jogador tenta adivinhar
print(f'{cores['roxo']}PROCESSANDO...{cores['limpa']}')
time.sleep(3)
if u == n:
    print('COMO VOCÊ CONSEGUIU???\nVocê acertou.')
else:
    print(f'{cores['vermelho']}GANHEI! Eu escolhi {cores['limpa']}{n}{cores['vermelho']} e você {cores['limpa']}{u}{cores['vermelho']}. TENTE NOVAMENTE!{cores['limpa']}')

#Analisando triangulo
r1 = float(input('Qual o tamanho da primeira reta: '))
r2 = float(input('Qual o tamanho da segunda reta: '))
r3 = float(input('Qual o tamanho da terceira reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'{cores['verde']}As retas acima FORMAM triângulo{cores['limpa']}')
else:
    print(f'{cores['vermelho']}As retas acima NÃO FORMAM triângulo{cores['limpa']}')

#Aumento múltiplo
s = float(input('Qual o salário do funcionário? '))

if s <= 1250.00:
    print(f'O salário {s} com aumento de 15% vai para R$ {s + (s*0.15):.2f}')
else:
    print(f'O salário {s} com aumento de 10% vai para R$ {s + (s*0.10):.2f}')

#Maior e menor
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

menor = v1
if v3<v2 and v3<v1:
    menor = v3
if v2<v1 and v2<v3:
    menor = v2
maior = v1
if v3>v2 and v3>v1:
    maior = v3
if v2>v1 and v2>v3:
    maior = v2
print(f'O menor número é: {menor} \nO maior número é: {maior}')

#Ano bissexto
ano = int(input('Escreva um ano para analisar (use 0 para o ano atual): '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} É BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')

#Radar eletrônico
v = float(input('Qual a velocidade do carro: '))
r = (v - 80) * 7
if v > 80.0:
    print(f'Você foi multado em R${r:.2f}, por estar acima do limite de velocidade, que é 80km/h.')
print('Ótimo dia, dirija com segurança!')
#Impar ou par
n1 = int(input('Escreva um número: '))

if n1 % 2:
    print(f'O número {n1} é IMPAR')
else:
    print(f'O número {n1} é PAR.')

#Custo da viagem
km = float(input('Qual a distancia da viagem? '))

if km <=200:
    print(f'O valor da passagem é de R$ {km*0.5:.2f}')
else:
    print(f'O valor da passagem é de R$ {km*0.45:.2f}')



