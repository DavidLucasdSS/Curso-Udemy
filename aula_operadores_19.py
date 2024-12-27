'''
Operadores relacionais
OP      SIGNIFICADO         EXEMPLO (True)
>       Maior               2 > 1
<       Menor               3 < 5
>=      Maior ou Igual      3 >= 1.5
<=      Menor ou Igual      2 <= 
==      Igual               1 == 1
!=      Diferente           1 != -1
'''

maior = 2 > 9
maior_ou_igual = 2 >= 0
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'

# Verificação adicional para comparar com False
todas_falsas = not (maior or menor or maior_ou_igual or menor_ou_igual or igual or diferente)

if maior and menor and maior_ou_igual and menor_ou_igual and igual and diferente:
    print('Todas as operações são verdadeiras.')
elif todas_falsas:
    print('Todas as operações são falsas!')
else:
    print('Pelo menos uma operação é verdadeira!')
