cores = {'':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[36m'}

msg = f'''{cores['amarelo']}Seja bem vindo(a) ao site do papai :boom::boom:
Meu primeiro site, sem julgamentos :boom::boom::boom:.{cores['']}'''
print(msg)

lista = ['aline', 'Aline', 'Aline Andrade', 'lirou ali', 'little ali', 'garbagepalekids']
nome = str(input(f'{cores['roxo']}Digite um nome: {cores['']}')).strip()
if nome == lista:
    print(f'{cores['ciano']}Boa, acerto!{cores['']}')
else:
    print(f'{cores['amarelo']}Se você digito o nome de outra menina, não tem jeito, dento também.. talves{cores['']}')
senha = str(input(f'{cores['roxo']}Digite sua senha: {cores['']}')).strip()
print(f'{cores['vermelho']}Sua senha é: {senha}:clown_face::knife::knife:')
print(f'{cores['vermelho']}Você foi hackeada pela tropa do palhaço careca :clown_face::clown_face::clown_face::knife::knife:{cores['']}')

