"""
    Some todos os números únicos de uma lista.
    Se um número aparecer na lista mais de uma vez, não o inclua na soma total.
"""
from utils import PerguntarSobre, continuar


def soma_numeros_unicos(lista) -> int:
    """
    Soma os números únicos de uma lista, não incluindo repetidos na soma
    :param lista: a lista a ser analidada
    :type lista: list
    :return: retorna a soma de todos os números únicos da lista
    """
    numeros_unicos = set()
    for n in lista:
        if lista.count(n) == 1:
            numeros_unicos.add(n)
    return sum(numeros_unicos)


RESPOSTA = ''
nlista = []

while RESPOSTA != 'n':
    nlista.append(PerguntarSobre.numeros_inteiros())
    RESPOSTA = continuar()

resultado = soma_numeros_unicos(nlista)

print(f'Os números digitados foram: {nlista}')
print(f'O resultado desses números, tirando as repetições, é {resultado}')
