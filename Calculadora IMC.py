print('----CALCULADORA DE IMC----')

p = float(input('Digite seu peso: '))
h = float(input('Digite sua altura: '))

hAoQuadrado = h*h
calculaImc = p/hAoQuadrado

print('Seu IMC é: ', calculaImc)