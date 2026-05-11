cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[36m'}

print('Some dois valores e mostre o resultado')
n1 = int(input(f'{cores['amarelo']}Mê de um número: '))
n2 = int(input(f'{cores['roxo']}Mê de mais um número: {cores['limpa']}'))
soma = n1 + n2
print(f'A soma entre {cores['amarelo']}{n1}{cores['limpa']} e {cores['roxo']}{n2}{cores['limpa']} vale {cores['verde']}{soma}{cores['limpa']}')

print('### AGORA DIGITE ALGO ###')
algo = (input())
print('Qual tipo primitivo deste valor? {}'.format(type(algo)))
print('Algo é uma palavra? {}'.format(algo.isalpha()))
print('Algo está escrito em letra maiuscula? {}'.format(algo.isupper()))
print('Algo está escrito em letra minuscula? {}'.format(algo.islower()))
print('Algo é númerico? {}'.format(algo.isnumeric()))
print('Algo é decimal? {}'.format(algo.isdecimal()))
print('Algo está vazio? {}'.format(algo.isspace()))
print('Algo é alfanumérico? {}'.format(algo.isalnum()))
print('Algo está capitalizada? {}'.format(algo.istitle()))

#n1, n2, soma, algo = são objetos