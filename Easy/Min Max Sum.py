from Biblioteca import numeros_inteiros, continuar
nlista = []


def min_max_sum(lista):
    print(f'O maior número é {max(lista)}\nO menor número é {min(lista)}\nA soma entre eles é', end=' ')
    print(max(lista)+min(lista))


resposta = ''
while resposta != 'n':
    nlista.append(numeros_inteiros())
    resposta = continuar()
min_max_sum(nlista)
