from Biblioteca import numeros_inteiros, continuar
def soma_numeros_unicos(lista):
    numeros_unicos = set()
    for n in lista:
        if lista.count(n) == 1:
            numeros_unicos.add(n)
    return sum(numeros_unicos)


nlista = []
resposta = ''
while resposta != 'n':
    nlista.append(numeros_inteiros())
    resposta = continuar()

resultado = soma_numeros_unicos(nlista)
print(f'Os números digitados foram: {nlista}')
print(f'O resultado desses números, tirando as repetições é {resultado}')
