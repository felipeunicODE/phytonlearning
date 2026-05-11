cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[36m'}

print(f'{cores['vermelho']}Olá, Mundo{cores['limpa']}')
msg = 'Olá, Mundo'
print('{}{}{}'.format( cores['amarelo'], msg, cores['limpa']))
