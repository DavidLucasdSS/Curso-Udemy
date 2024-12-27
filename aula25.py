"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luis'
preco_whey = 99.00
preco_creatina = 103.50
frete = 12.00
total = preco_whey + preco_creatina + frete
variavel = '%s, o preço do Whey é de R$%.2f, a CREATINA(250G) CREAPURE® R$%.2f e o frete ficou em R$%.2f.' % (nome, preco_whey, preco_creatina, frete)
print(f'{variavel} O valor total foi de {total}')


print('O hexadecimal de %d é %X' % (215, 215))