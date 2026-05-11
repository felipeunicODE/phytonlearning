#Análise de texto
nome = str(input('Digite um nome: ')).strip()
nomed = nome.split()
print(f'Seu nome em maiusculo: {nome.upper()}')
print(f'Seu nome em minusculo: {nome.lower()}')
print('Quantas letras seu nome possui: {} vezes'.format(len(nome) - nome.count(' ')))
print(f'Quantas letras tem o primeiro nome: {nomed[0]}')
print(f'Seu primeiro nome é: {nomed[0]}\nSeu último nome é: {nomed[-1]}')
print('SILVA' in nome.upper())

#Digitos de um número

numero = int(input('Digite um número: '))
print(f'Unidade: {numero // 1 % 10}')
print(f'Dezena: {numero // 10 % 10}')
print(f'Centena: {numero // 100 % 10}')
print(f'Milhar: {numero // 1000 % 10}')

#Verificar se há algo especifico na frase ou não.

cidade = str(input('Digite uma cidade: ')).strip().upper()
print(cidade[:5].upper() == 'SANTO' or 'SANTO' in cidade)

#Quantidade de letra, onde aparece pela primeira e ultima vez.

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ','')
frasel = frase.replace('Á', 'A').replace('Â', 'A').replace('À', 'A').replace('Ã', 'A').replace('É', 'E').replace('Ê', 'E').replace('È', 'E').replace('Í', 'I').replace('Î', 'I').replace('Ì', 'I').replace('Ó', 'O').replace('Ô', 'O').replace('Ò', 'O').replace('Õ', 'O').replace('Ú', 'U').replace('Û', 'U').replace('Ù', 'U')
letra = str(input('Digite a letra que gostaria de fazer a analise: ')).strip().upper()
print('A frase escrita tem {} letras {}'.format(frasel.count(letra), letra))
print('A primeira letra {} apareceu na posição: {}'.format(letra, frasel.find(letra)+1))
print('A última letra {} apareceu na posição: {}'.format(letra, frasel.rfind(letra)+1))

