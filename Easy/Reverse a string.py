"""
    Escreva o inverso de uma palavra
"""

from utils import PerguntarSobre


def reverse(string):
    """
    Inverte uma string.
    :param string: A palavra ou string informada
    :return: retorna o inverso da string
    """
    return string[::-1]


PALAVRA = PerguntarSobre.strings()

print(f'O reverso de {PALAVRA} é {reverse(PALAVRA)}')
