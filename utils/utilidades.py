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
            if r == 'n' or r == 's':
                return r
            else:
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
        Pergunta ao usúario uma PALAVRA em
        :return:
        """
        while True:
            try:
                n = int(input('Digite um número inteiro: '))
            except (ValueError, TypeError):
                mensagem_erro()
                continue
            else:
                return n

    @staticmethod
    def strings() -> str:
        """
        Pergunta ao usúario uma PALAVRA em valor string.
        Valores não string seriam como: ¹, None, etc.
        :return: o valor string informado pelo usúario
        """
        while True:
            try:
                s = str(input('Digite uma PALAVRA (string): '))
            except (ValueError, TypeError):
                mensagem_erro()
                continue
            else:
                return s
