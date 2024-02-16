"""
    O usúario pode escolher se ele gostaria de aninhar uma lista dentro de outra.
    Com isso, informe a lista criada pelo usúario e a lista aplanada
"""

from utils import PerguntarSobre, continuar


def flatten(lista):
    """
    Remove os aninhamentos da lista e retorna a lista aplanada.
    :param lista: lista informada
    :return: retorna a lista aplanada
    """
    listaunica = []
    for elemento in lista:
        if isinstance(elemento, list):
            listaunica.extend(flatten(elemento))
        else:
            listaunica.append(elemento)
    return listaunica


def nova_lista():
    """
    Cria uma lista e dentro da função, o usúario irá informar os valores (números) a serem colocados
    :return: retorna o valor da lista criada
    """
    lista = []
    R = ''
    while R != 'n':
        lista.append(PerguntarSobre.numeros_inteiros())
        R = continuar()
    return lista


listar = [[]]
C = 0
RESPOSTA = RESPOSTALISTA = ''

while RESPOSTA != 'n':
    listar[C].append(PerguntarSobre.numeros_inteiros())
    RESPOSTA = continuar()
    RESPOSTALISTA = continuar('Você gostaria de criar uma lista aninhada?')
    if RESPOSTALISTA == 's':
        listar.append(nova_lista())
print(f'Lista principal: {listar}\nLista aplanada: {flatten(listar)}')
