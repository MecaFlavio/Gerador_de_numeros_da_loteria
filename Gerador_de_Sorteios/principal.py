import funçoes_loteria

# Variaveis
resposta = ''
confirma = True
continuar = True

while continuar:

    opção = funçoes_loteria.cabeçalho()
    while opção < 1 or opção > 4:
        try:
            if opção < 1 or opção > 4:
                print('Opção não identificada, tente novamente...')
                opção = funçoes_loteria.cabeçalho()
            else:
                break
        except ValueError:
            print('Opção não identificada, tente novamente...')
            opção = funçoes_loteria.cabeçalho()
    if opção == 1:
        funçoes_loteria.num_max = 60
        funçoes_loteria.regras(6, 15)
    elif opção == 2:
        funçoes_loteria.num_max = 25
        funçoes_loteria.regras(15, 20)
    elif opção == 3:
        funçoes_loteria.num_max = 80
        funçoes_loteria.regras(5, 15)
    elif opção == 4:
        funçoes_loteria.num_max = 100
        funçoes_loteria.regras(lotomania=True)

    print('Deseja realizar mais jogos?')
    resposta = str(input('Ditige S (SIM) ou N (NÃO):  ')).strip().upper()
    confirma = True
    while confirma:
        if resposta == 'S':
            confirma = False
        elif resposta == 'N':
            confirma = False
        else:
            print('Resposta não identificada.\nDeseja Realizar mais jogos?')
            resposta = str(input('Digite S (SIM) ou N (NÃO): ')).strip().upper()
    if resposta == 'N':
        continuar = False
    print('Obridado. Até Logo!')
