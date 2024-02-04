from Biblioteca import numeros_inteiros, continuar


def flatten(lista):
    listaunica = []
    for elemento in lista:
        if isinstance(elemento, list):
            listaunica.extend(flatten(elemento))
        else:
            listaunica.append(elemento)
    return listaunica


def lista_aninhada():
    lista = []
    resposta2 = ''
    while resposta2 != 'n':
        lista.append(numeros_inteiros())
        resposta2 = continuar()
    return lista


listar = [[]]
c = 0
resposta = respostalista = ''

while resposta != 'n':
    listar[c].append(numeros_inteiros())
    resposta = continuar()
    respostalista = continuar('Você gostaria de criar uma lista aninhada?')
    if respostalista == 's':
        listar.append(lista_aninhada())
print(f'Lista principal: {listar}\nLista aplanada: {flatten(listar)}')
