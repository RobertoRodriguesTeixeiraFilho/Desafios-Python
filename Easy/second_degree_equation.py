"""
    Escreva um programa que resolva uma equação de segundo grau. 
"""
from utils import PerguntarSobre, continuar

def second_degree_equation(a, b, c):
    """
    Calcula uma equação de segundo grau
    :return: 2 raízes, se delta for positivo, 1 se for nulo e nenhuma, se negativo
    """
    delta = b**2 - 4*a*c

    if delta < 0:
        print('A equação não possui raízes reais.')
        return None
    elif delta == 0:
        x = -b / (2 * a)
        return x
    else:
        raiz_delta = delta**1/2
        x1 = (-b + raiz_delta)/ (2*a)
        x2 = (-b - raiz_delta)/ (2*a)
        return x1, x2


R = ''
A = B = C = 0
while R != 'n':
    A = PerguntarSobre.numeros_inteiros()
    B = PerguntarSobre.numeros_inteiros()
    C = PerguntarSobre.numeros_inteiros()
    print(f'A equação ficará: {A}x² + ({B})x + ({C}) = 0')

    R = continuar('Você gostaria de trocar todos os valores?')

raizes = second_degree_equation(A, B, C)

if raizes is not None:
    print('Raízes:', end='')
    if isinstance(raizes, tuple):
        print(raizes[0], end=', ')
        print(raizes[1])
    else:
        print(raizes)
