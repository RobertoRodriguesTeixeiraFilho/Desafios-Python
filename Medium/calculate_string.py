"""
    Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
"""
from utils import PerguntarSobre, mensagem_erro


def calculate_string(numero1, numero2, sinal):
    """
    Calcula dois números com a operação matemática definida pelo sinal
    :return: retorna o resultado
    """
    operadores ={
        '+': 'soma',
        '-': 'subtração',
        '*': 'multiplicação',
        '/': 'divisão'
    }

    if sinal in operadores:
        try:
            operacao = operadores[sinal]
            expressao = f"{numero1} {sinal} {numero2}"
            resultado = eval(expressao)
            return {"resultado": resultado, "operação": operacao}
        except ZeroDivisionError:
            mensagem_erro('Divisão por zero não é aceita')
    else:
        return False


N = []

for c in range(0, 2):
    N.append(PerguntarSobre.numeros_inteiros())


S = input('Digite o sinal que você gostaria de usar na operação (+, -, *, /):')

equacao = calculate_string(N[0], N[1], S)

if equacao:
    print(f'{equacao["operação"]} entre {N[0]} e {N[1]} = {equacao["resultado"]}')
else:
    mensagem_erro()
