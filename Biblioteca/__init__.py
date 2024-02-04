def mensagem_erro():
    print('Erro! Digite uma resposta válida')


def continuar(pergunta='Gostaria de continuar?'):
    while True:
        try:
            r = str(input(f'{pergunta} [s/n]')).lower().strip()[0]
        except:
            mensagem_erro()
            continue
        else:
            if r == 'n' or r == 's':
                return r
            else:
                mensagem_erro()


def numeros_inteiros():
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            mensagem_erro()
            continue
        else:
            return n


def strings():
    while True:
        try:
            s = str(input('Digite uma palavra (string): '))
        except (ValueError, TypeError):
            mensagem_erro()
            continue
        else:
            return s

