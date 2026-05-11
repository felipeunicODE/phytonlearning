import math, random
#Numero real para inteiro
num = float(input('Digite um número real: '))
nr = math.trunc(num)
print(f'O número digitado foi {num} e sua parte inteira é {nr}')

#Sorteio de item
n1 = str(input('Primeiro aluno: ')).strip()
n2 = str(input('Segundo aluno: ')).strip()
n3 = str(input('Terceiro aluno: ')).strip()
n4 = str(input('Quarto aluno: ')).strip()
lista = [n1, n2, n3, n4]
print(f'O escolhido para apagar o quadro foi: {random.choice(lista)}')

#Sorteio de ordem
#Eu já tenho o nome dos alunos, utilizei o shuffle para embaralhar e mostrei a lista
random.shuffle(lista)
print(f'O grupo dos alunos apresentarão o trabalho na ordem: \n{lista}')

n = float(input('Escreva um número real: '))
print(f'O número {n} convertido para inteiro é igual a {math.trunc(n)}.')

#Hipotenusa

ca = float(input('Escreva o valor do cateto adjascente: '))
co = float(input('Escreva o valor do cateto oposto: '))
h = math.hypot(ca, co)
print(f'O cateto adjascente é: {ca}\nO cateto oposto é: {co}\nO comprimento da hipotenusa é: {h:.2f}')

#Seno, Cosseno e Tangente O número deve ser convertido para radiano e posteriormente feito o calculo.

ang = float(input('Escreva o valor de um ângulo qualquer: '))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print(f'O angulo {ang}° tem o valor de seno {seno:.2f}\nO ângulo de {ang}° tem o valor de cosseno {cosseno:.2f}\nO ângulo de {ang}° tem o valor da tangente {tangente:.2f}')


