import random

num_max = int


def separador():
    """
    Cria uma moldura com finalidade de organizar a apresentaçao do programa.
    :return: String com 30 x '='
    """
    print('=' * 30)


def cabeçalho():
    separador()
    print(f"{'Gerador de Sorteios':^30}")
    separador()
    print('''QUAL JOGO DESEJA APOSTAR:
 [1] - Mega Sena: Aposta de 6 a 15 números entre 60
 [2] - Loto Facil: Apósta de 15 a 20 numeros entre 25
 [3] - Quina: Apósta de 5 a 15 números entre 80
 [4] - Lotomania: Apósta 50 números''')
    while True:
        try:
            opção = int(input('Digite a opção desejada: '))
            while opção < 1 or opção > 4:
                if opção < 1 or opção > 4:
                    print('Opção não identificada, tente novamente...')
                    opção = int(input('Digite a opção desejada: '))
            separador()
            return opção
        except ValueError:
            print('Opção não identificada, tente novamente...')
            continue
    separador()


def regras(aposta_min=int(), aposta_max=int(), lotomania=False):
    """
    Realiza a escolha randomica de quantidades de números para cada jogo e cria uma string
    com os números selecionados.
    :param aposta_min: Quantidade minimo de números na aposta para o jogo ecolhido.
    :param aposta_max: Quantidade maxima de números na aposta paro o jogo escolhido.
    :param lotomania: Se loto mania ativado quantidade de numeros será 50.
    :return: seguencia de string concatenada de números para o jogo escolhido,
    """
    jogo = 0
    sorteio = 0
    contador = 0
    apósta = 50
    numeros = []
    resultado = ''
    if not lotomania:
        while sorteio <= 0:
            try:
                print('Quantos NÚMEROS quer apostar?')
                apósta = int(input(f'{aposta_min} até {aposta_max}: '))
                while apósta < aposta_min or apósta > aposta_max:
                    print(f'Quantidade incorreta! Escolha de {aposta_min} a {aposta_max} numeros.')
                    apósta = int(input('Quantos números quer apostar: '))
                sorteio = apósta
            except ValueError:
                print('Opção não identificada, tente novamente...')
                continue
    else:
        sorteio = apósta
    while sorteio > 0:
        jogo = random.randint(1, num_max)
        numeros.append(jogo)
        contador = numeros.count(jogo)
        if contador > 1:
            numeros.pop()
        elif contador == 1:
            sorteio -= 1
    numeros.sort()
    for i in range(0, apósta):
        resultado += str(numeros[i]) + ' '
    print(f'Seu jogo da MEGA SENA SERÁ: \n{resultado}')