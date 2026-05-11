import emoji

print(emoji.emojize('Olá, Mundo! :globe_showing_Americas:'))

cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'cinza':'\033[36m'}

#print('Irei lhe fazer algumas perguntas.')
#nome = str(input('Qual seu nome? '))
#idade = int(input('Qual sua idade? '))
#peso = float(input('Qual seu peso? '))
#print('Certo, peguei suas armazenei você é o(a): Nome: {}, Idade: {}, Peso: {}Kg'.format(nome, idade, peso))
# nome, idade, peso = são rótulos das caixas
#nome = input('Qual seu nome? ')
#print('Olá', nome,'! Prazer em te conhecer!')
# as variaveis são o código, por exemplo Nome = input irá solicitar para o usuário preencher alguma informação
#print('Quando você nasceu?')
#dia = input('Dia: ')
#mes = input('Mês: ')
#ano = input('Ano: ')

#print('Você nasceu no dia {} de {} de {}.'.format(dia, mes, ano))

#print('Agora somaremos dois números.')
#primeiro_numero = int(input('Primeiro número '))
#segundo_numero = int(input ('Segundo número '))
#soma_dos_numeros = primeiro_numero + segundo_numero
#print('A soma entre {} e {} vale: {}'.format(primeiro_numero, segundo_numero, soma_dos_numeros))
##EXEMPLO DO VÍDEO
#n1 = input('Digite um número: ')
#n2 = input('Digite mais um número: ')
#s = n1 + n2
#print('A soma dos dois números é: ', s) - Não irá somar, pois n1 e n2 estão com string e não está convertida para inteiro/float

##CÓDIGO CORRETO
#n1 = int(input('Digite um número: '))
#n2 = int(input('Digite mais um número: '))
#s = n1 + n2
#print('A soma entre',n1,'e',n2, 'vale',s)
#print('A soma entre {} e {} vale {}'.format(n1,n2,s))

#CONCEITOS PRIMITIVOS
#int = transformar texto (str) em número (7, -4).
#float = transformar texto (str) em número decimal (0.5, -15.333, 7.0)
#bool = True False
#str = 'Olá', '7,5', ''
# {} + .format() = forma de utilizar a sintaxe de print e substituir as informações que precisam ser mostradas

#OPERADORES ARITIMÉTICOS
# + Adição 5 + 2 == 7
# - Subtração 5 - 2 == 3
# * Multiplicação 5 * 2 == 10
# ** Potência = 5 ** 2 == 25
# // Divisão inteira = 5//2 == 2
# % Restante da divisão = 5%2 == 1

#ORDEM DE PRECEDÊNCIA
# () 1º
# ** 2º
# * / // % 3º
# + - 4º
#EXEMPLO
#n1 = int(input('Primeiro número: '))
#n2 = int(input('Segundo número: '))
#n3 = int(input('Terceiro número: '))
#n4 = int(input('Quarto número: '))

#calculo1 = n1+n2*n3
#calculo2 = n3*n1+n4**n2
#calculo3 = n3*(n1+n4)**n2
## 5 2 3 4 (Ordem para bater com os resultados do vídeo)
#print('O resultado dos calculos são: 1- {}, 2- {}, 3- {}'.format(calculo1, calculo2, calculo3))

#print('Esta é uma calculadora com dois números inteiros e ela da o resultado das prinicipais funções aritiméticas e algumas formatações')
#numero1 = float(input('Primeiro numero: '))
#numero2 = float(input('Segundo numero: '))
#numero3
#m = numero1 + numero2
#s = numero1 - numero2
#v = numero1 * numero2
#d = numero1 / numero2
#e = numero1 ** numero2
#di = numero1 // numero2
#r = numero1 % numero2

#print('O resultado da soma é {:<5}, subtração {:^10}, multiplicação \n{:5>} e divisão {:.3f}'.format(m, s, v, d), end='. ')
#print('O resultado da \nexponenciação é {:^35}, divisão inteira {:50}, e resto da divisão {}'.format(e, di, e))

##não necessariamente preciso aplicar a formula aritimética em uma variavel, posso aplicar diretamente no format se for preciso mostrar naquela linha.

##end='' = Não quebra a linha
##\n = Quebra a linha aonde aplicado
##: Aplica caracter
##> Alinhamento a direita
##< Alinhamento a esquerda
##^ Alinhamento no centro
##Qualquer caracter aplicado a esquerda dos demais será preenchido como tal
##Se a variavel estiver como float, int eu posso mostrar ela como str usando desta forma (f' blablabla {variavel de float:}') não necessariamente preciso colocar dois pontos mas após os dois pontos é a formatação da variavel float na str.

#O comando import serve para para importar dados e o from eu posso especificar o que quero do banco de dados.
#import - generalista
#from = import - especifico
#math é uma biblioteca padrão, que ja vem no Phyton e ela tem as funcionalidades (ceil (arredonda pra cima), floor (arredonda pra baixo), trunc (elimina da virgula p tras), pow (potência), sqrt (raiz quadrada), factorial.
#import com from, não necessita utilizar a referência da importação

#Manipulando cadeia de textos

#Fatiamento

#frase[9:13] - Nome da variavel e entre colchetes o número do micro espaço do indice daquela str
#Utiliza-se : para delimitar o inicio e o fim da marcação do micro espaço da variavél;
# :: dentro do colchete significa que a marcação será pulando a quantidade indicada no colchete.

#Análise

#len(frase) = Comprimento da str
#frase.count('o') = Conta as letras especificadas no parentese
#frase.find('deo') = Busca a junção de letras especificadas no parentese e encontra a posição onde ela se inicia nos micros espaços
#Caso a junção de letras não esteja na str retornará o sinal de -1 (não existe na str)

#in = 'Curso' in frase = ira buscar Curso na variavel frase = True

#Transformação

#frase.replace('Phyton, Android') = Substitui a 1a pela 2a
#frase.uper() = O que já for maiusculo mantem o que for minusculo altera
#frase.lower() = O que ja for minusculo mantem o que for maiusculo altera
#frase.capitalize() = Primeira letra em maiusculo restante minusculo
#frase.title() = Todas as letras em maiusculo pós espaço
#frase.strip() = Remove espaços inúteis
#frase.rstrip() = Remove os espaços inuteis da direita somente
#frase.lstrip() = Remove os espaços inuteis da esquerda somente

#Divisão
#frase.split() = Cada palavra recebe uma nova indexação e cada indexação tem uma numeração
#'-'.join(frase) = Junta as indexações separadas em um novo grupo e pode colocar um caracter nos espaços vazios

#""" = Seleciona o texto inteiro
#frase = 'Curso em Vídeo Phyton'
#print(frase[3::2])

#Condições - Simples e Compostas, Condição Simplificada (Phyton)
#objeto.metodo()

#if objeto.metodo: #bloco Verdadeiro

#    else #bloco Falso #estruta composta
#objeto.metodo #se a estrutura estiver alinhada a esquerda acontecerá sempre
               #se a estrutura estiver pra dentro da condição.

#tempo = int(input('Quantos anos tem seu carro: '))
#if tempo <=3:
    #print('Carro novo') #Bloco verdadeiro
#else:
    #print('Carro velho') #Bloco falso
#print('--FIM--')

#Condição simplificada:
#tempo = int(input('Quantos anos tem seu carro: '))
#print('Carro novo'if tempo<=3else'carrovelho')
#print('--FIM--')

#Cores no terminal
#Código ANSI \033[0 (style);33 (cor do texto);44 (cor do fundo)m #Qualquer ordem,
#Style (Estilo do texto)
#0 none
#1 bold
#4 underline
#7 negativo
#Text (Cor do texto)
#30 branco
#31 vermelho
#32 verde
#33 amarelo
#34 azul
#35 roxo
#36 ciano
#37 cinza
#Background (Fundo da letra)
#40 branco
#41 vermelho
#42 verde
#43 amarelo
#44 azul
#45 roxo
#46 ciano
#47 cinza

