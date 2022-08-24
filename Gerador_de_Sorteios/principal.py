import random


# Variaveis
global numeros, resultado, num_max
resposta = ''
confirma = 0
continuar = True


def separador():
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
    separador()


def regras(aposta_min=int(), aposta_max=int(), lotomania=False):
    jogo = 0
    sorteio = 0
    contador = 0
    apósta = 50
    numeros = []
    resultado = ''
    if not lotomania:
        separador()
        print('Quantos NÚMEROS quer apostar?')
        apósta = int(input(f'{aposta_min} até {aposta_max}: '))
        while apósta < aposta_min or apósta > aposta_max:
            print(f'Quantidade incorreta! Escolha de {aposta_min} a {aposta_max} numeros.')
            apósta = int(input('Quantos números quer apostar: '))
        sorteio = apósta
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


while continuar:

    cabeçalho()

    opção = int(input('Digite a opção desejada: '))
    while opção < 1 or opção > 4:
        if opção < 1 or opção > 4:
            print('Opção não identificada, tente novamente...')
            cabeçalho()
            opção = int(input('Digite a opção desejada: '))
        else:
            break
    if opção == 1:
        num_max = 60
        regras(6, 15)
    elif opção == 2:
        num_max = 25
        regras(15, 20)
    elif opção == 3:
        num_max = 80
        regras(5, 15)
    elif opção == 4:
        num_max = 100
        regras(lotomania=True)

    print('Deseja realizar mais jogos?')
    resposta = str(input('Ditige S (SIM) ou N (NÃO):  ')).strip().upper()
    confirma = 0
    while confirma == 0:
        if resposta == 'S':
            confirma = 1
        elif resposta == 'N':
            confirma = 2
        else:
            while resposta != 'S' or resposta != 'N':
                print('Resposta não identificada.\nDeseja Realizar mais jogos?')
                resposta = str(input('Digite S (SIM) ou N (NÃO): ')).strip().upper()
                break
    if confirma == 1:
        continue
    if confirma == 2:
        continuar = False
