"""
    Verifique se uma string é balanceada.
    Para uma string ser balanceada, todas as palavras que contêm em uma tem que estar em outra.
"""

from utils import PerguntarSobre


def is_balanced(primeiro, segundo) -> bool:
    """
    Verifica se as letras de duas palavras são repetidas uma em outra.
    :param primeiro: primeira palavra informada
    :param segundo: segunda palavra informada
    :return: retorna se a verificação foi falsa ou verdadeira.
    """
    return set(primeiro).issubset(set(segundo)) or set(segundo).issubset(set(primeiro))


strlista = []

for c in range(0, 2):
    strlista.append(PerguntarSobre.strings())

valor = is_balanced(strlista[0], strlista[1])

if valor is True:
    print('Essas strings são balanceadas')
if valor is False:
    print('Essas strings não são balanceadas')

print('Para uma string ser balanceada, todas as palavras que contêm em uma tem que estar em outra.')
