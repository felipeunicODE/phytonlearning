cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[36m'}

nome = (input(f'{cores['verde']}Digite seu nome: ')).strip()
print(f'{cores['azul']}É um prazer te conhecer, {cores['ciano']}{nome}{cores['azul']}!') ## Posso utilizar o código desta forma "print('Texto, {}!'.format(nome))
                                                                                        ## O colchete será substituido pela variavel