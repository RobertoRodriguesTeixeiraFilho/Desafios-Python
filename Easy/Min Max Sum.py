"""
    Retorne o menor e o maior valor de uma lista de números
"""

from utils import PerguntarSobre, continuar

def min_max_sum(lista):
    """
    Informa qual é o maior número e o menor de uma lista e a soma entre eles.
    :param lista: A lista de números a ser informada pelo usúario.
    :return: sem retorno
    """
    print(f'O maior número é {max(lista)}\nO menor número é {min(lista)}\nA soma entre eles é', end=' ')
    print(max(lista)+min(lista))


RESPOSTA = ''
nlista = []

while RESPOSTA != 'n':
    nlista.append(PerguntarSobre.numeros_inteiros())
    RESPOSTA = continuar()
min_max_sum(nlista)
