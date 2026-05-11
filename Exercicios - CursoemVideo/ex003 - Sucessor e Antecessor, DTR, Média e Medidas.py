#Sucessor e Antecessor
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('O antecessor de {} é {} \nO sucessor de {} é {}'.format(n, a, n, s))

#Dobro, triplo e raiz
print('='*20)
print('O dobro de {} é {}\nO triplo de {} é {}\nA raiz quadrada de {} é {:.2f}'.format(n, n*2, n, n*3, n, n**(1/2)))

#Média Aritimética
print('='*20)
p = float(input('Coloque a nota de Português: '))
m = float(input('Coloque a nota de Matemática: '))

print('A média entre {:.1f} e {:.1f} é: {:.1f}'.format(p, m, (p + m) / 2))

#Conversor de medidas
print('='*20)
medida = float(input('Uma distância em metros: '))
km = medida / 1000 #kilometro
hm = medida / 100 #hectometro
dam = medida / 10 #decametro
dm = medida * 10 #decimetro
cm = medida * 100 #centimetro
mm = medida * 1000 #milimetro
print("A medida de {}m corresponde a \n{}km \n{}hm \n{}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm".format(medida, km, hm, dam, dm, cm, mm))

