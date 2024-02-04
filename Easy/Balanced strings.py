from Biblioteca import strings


def is_balanced(primeiro, segundo):
    return set(primeiro).issubset(set(segundo)) or set(segundo).issubset(set(primeiro))


strlista = []
resposta = ''

for c in range(0, 2):
    strlista.append(strings())
valor = is_balanced(strlista[0], strlista[1])

if valor is True:
    print('Essas strings são balanceadas')
if valor is False:
    print('Essas strings não são balanceadas')
print('Para uma string ser balanceada, todas as palavras que contêm em uma tem que estar em outra.')
