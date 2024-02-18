"""
    Módulo de utilidades

    Este módulo contém funções utilitárias para interações com o usuário.
"""


def mensagem_erro() -> None:
    """
    Mostrará uma mensagem de erro ao usúario
    """
    print('Erro! Digite uma RESPOSTA válida')


def continuar(pergunta='Gostaria de continuar?') -> str:
    """
    Pergunta ao usúario se ele gostaria de continuar a rodar o programa

    :param pergunta: a pergunta a ser feita para o usúario , a padrão é 'Gostaria de continuar?'
    :type pergunta: str

    :return: retorna a RESPOSTA, caso o usúario informe corretamento [s/n]
    """
    while True:
        try:
            r = str(input(f'{pergunta} (digite sim ou não): ')).lower().strip()[0]
        except (ValueError, TypeError):
            mensagem_erro()
            continue
        else:
            if r != '' and r in ('n', 's'):
                return r
            # Se o if não for seguido, não haverá retorno, portanto:
            mensagem_erro()


class PerguntarSobre:
    """
    Classe que fornece métodos seguros para lidar com entradas de dados do usúario

    Métodos:
    - numeros_inteiros() -> int: Solicita ao usuário para digitar um número inteiro.
                                 Retorna o número inteiro digitado.

    - strings() -> str: Pergunta ao usuário uma palavra em valor string.
                       Retorna a string informada pelo usuário.
    """
    @staticmethod
    def numeros_inteiros() -> int:
        """
        Pergunta ao usúario um número inteiro.
        Valores não inteiro seriam coomo: 1.5, ², strings, etc.
        :return: o valor inteiro informado pelo usúario
        """
        while True:
            try:
                n = int(input('Digite um número inteiro: '))
                return n
            except (ValueError, TypeError):
                mensagem_erro()
                continue

    @staticmethod
    def strings() -> str:
        """
        Pergunta ao usúario uma PALAVRA em valor string.
        Valores não string seriam como: ¹, None, etc.
        :return: o valor string informado pelo usúario
        """
        while True:
            try:
                s = input('Digite uma PALAVRA (string): ')
                return s
            except (ValueError, TypeError):
                mensagem_erro()
                continue
