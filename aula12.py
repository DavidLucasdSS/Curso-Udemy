#EXERCICIO - CÁLCULO DO IMC

nome = input('Qual é o seu nome? ')
altura = float(input('E a sua altura em metros? '))
massa = float(input('Quanto tens de massa? '))

IMC = massa / (altura ** 2)

print(f"{nome} possui uma altura de {altura}m com {massa}kg. Possui um IMC de {IMC=:.4f}(kg/m^2)")