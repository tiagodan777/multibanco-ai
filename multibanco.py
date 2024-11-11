from time import sleep


def utilizador_existe(banco):
    print()
    utilizador = str(input('Utilizador: '))
    for c in range(0, len(banco)):
        if banco[c][0] == utilizador:
            return utilizador
        else:
            if c == len(banco) - 1:
                while True:
                    print('\033[31mERRO! Utilizador não encontrado\033[m')
                    utilizador = str(input('Utilizador: '))
                    for i in range(0, len(banco)):
                        if banco[i][0] == utilizador:
                            return utilizador


def pass_correta(user, pw, banco):
    for c in range(0, len(banco)):
        if banco[c][0] == user:
            if banco[c][1] == pw:
                return
            else:
                while True:
                    print('\033[31mERRO! Password incorreta\033[m')
                    password = int(input('Password: '))
                    for i in range(0, len(banco)):
                        if banco[i][0] == user:
                            if banco[i][1] == password:
                                return


def retornar_os_dados_do_utilizador(user, banco):
    for c in range(0, len(banco)):
        if banco[c][0] == user:
            return banco[c]


def linha():
    for c in range(0, 2):
        print('='*80)


def primeira_inicializacao_do_multibanco():
    print()
    sleep(0.4)
    for c in range(0, 3):
        print('.', end="")
        sleep(0.3)
    print()
    print()
    print('Login Correto')
    print()


def inicializar_o_multibanco(limite=0, lista=0, espera=0):
    if espera == 0:
        sleep(0.6)
    print(f'{"MULTIBANCO":^80}')
    linha()
    print()
    # sleep(0.5)
    print('OPÇÕES DISPONÍVEIS')
    print()
    cont = 0
    if limite == 0:
        print('[1] - 10€\n'
              '[2] - 20€\n'
              '[3] - 50€\n'
              '[4] - 100€\n'
              '[5] - 200€\n'
              '[6] - Levantamentos de outras importâncias\n'
              '[7] - Ver os movimentos\n')
        cont = 7
    elif limite == 1:
        # print('OK')
        for c in range(0, len(notas_disponiveis)):
            if notas_disponiveis[c] <= (400 - lista):
                print(f'[{c+1}] - {notas_disponiveis[c]}€')
                cont += 1
        if cont > 0:
            mostrar_cont = cont
            print(f'[{mostrar_cont+1}] - Levantamentos de outras importâncias')
            print(f'[{mostrar_cont+2}] - Ver os movimentos')
            cont += 2
        else:
            mostrar_cont = cont
            print(f'[{mostrar_cont+1}] - Ver os movimentos')
            cont += 1
        print()

    return cont


def verificacao_da_opcao_de_levantamento(possibilidade_de_op):
    # print(possibilidade_de_op)
    opcao = int(input('Opção desejada: '))

    if opcao < 1 or opcao > possibilidade_de_op:
        valida = False
        while not valida:
            print('\033[31mERRO! Opção inválida\033[m')
            opcao = int(input('Opção desejada: '))

            # print(possibilidade_de_op)
            # print(opcao)
            if opcao > 0 and opcao <= possibilidade_de_op:
                valida = True
    return opcao - 1


def opcao_de_levantamento(op, lista, possibilidade_de_op):
    # print('OKOK')
    dinheiro_a_ser_levantado = ''
    notas_disponiveis_internas = notas_disponiveis.copy()
    notas_disponiveis_mostrar = []
    calculo = 7 - possibilidade_de_op
    # print(calculo)

    for c in range(0, calculo-1):
        notas_disponiveis_internas.pop()

    if len(notas_disponiveis_internas) > 0:
        # print(dados[2])
        for c in range(0, len(notas_disponiveis)):
            if notas_disponiveis[c] <= (400 - dados[2]):
                # print(f'dados[2]: {dados[2]}')
                # print(f'notas diposniveis mostar: {notas_disponiveis_mostrar}')
                notas_disponiveis_mostrar.append(notas_disponiveis[c])
        if calculo == 0:
            if op < len(notas_disponiveis_internas):
                # print('OKOKOK')
                # print(f'Len: {len(notas_disponiveis_internas)}')
                # print(notas_disponiveis_internas)
                dinheiro_a_ser_levantado = lista[op]
            elif op == len(notas_disponiveis_internas) and len(notas_disponiveis_internas) > 0:
                # print('ok')
                # print(notas_disponiveis_internas)
                dinheiro_a_ser_levantado = int(input(f'Que quantia desejas levantar?'
                                                     f' [entre 10€ e {notas_disponiveis_mostrar[-1]}]: '))
                temp = str(dinheiro_a_ser_levantado)

                if temp[-1] in '123456789' or dinheiro_a_ser_levantado < 10 or dinheiro_a_ser_levantado > notas_disponiveis_mostrar[-1]:
                    teste = False
                    while not teste:
                        if temp[-1] in '123456789':
                            if temp[-1] in '12':
                                print(f'\033[33mNão existem moedas de {temp[-1]}'
                                      f'€ disponíveis no multibanco. Selecione apenas múltiplos de 10\033[m')
                            elif temp[-1] == '5':
                                print(f'\033[33mNão existem notas de {temp[-1]}'
                                      f'€ disponíveis no multibanco. Selecione apenas múltiplos de 10\033[m')
                            else:
                                print(f'\033[33mNão é possível lenvantar valores cujo'
                                      f' o último algarismo seja {temp[-1]}€. Selecione apenas múltiplos de 10\033[m')
                        else:
                            print(f'\033[31mERRO! Por favor digita quantias apenas'
                                  f' entre 10€ e {notas_disponiveis_mostrar[-1]}€\033[m')
                        dinheiro_a_ser_levantado = int(input(f'Que quantia desejas'
                                                             f' levantar? [entre 10€ e {notas_disponiveis_mostrar[-1]}€]: '))
                        temp = str(dinheiro_a_ser_levantado)

                        if dinheiro_a_ser_levantado >= 10 and dinheiro_a_ser_levantado\
                                <= notas_disponiveis_mostrar[-1] and temp[-1] not in '123456789':
                            teste = True

            elif op == len(notas_disponiveis_internas) + 1:
                dinheiro_a_ser_levantado = - 1
                #print(dados[3][1])
                print()
                print('$ - '*15)
                print()
                if dados[3][0] != []:
                    for c in range(0, len(dados[3][0])):
                        print(f'Levantaste {dados[3][0][c]}€')
                else:
                    print('Ainda não efetuaste nenhum levantamento')
                    print()

                    return dinheiro_a_ser_levantado

                print('$ - ' * 15)
                print()

            return dinheiro_a_ser_levantado
        else:
            for c in range(0, len(notas_disponiveis)):
                if notas_disponiveis[c] <= (400 - dados[2]):
                    # print(f'dados[2]: {dados[2]}')
                    # print(f'notas diposniveis mostar: {notas_disponiveis_mostrar}')
                    notas_disponiveis_mostrar.append(notas_disponiveis[c])
                    
            # print(len(notas_disponiveis_internas))
            # print(f'CALCULO: {calculo}')
            if op < len(notas_disponiveis_internas) - 1:
                # print('OKOKOK')
                # print(f'Len: {len(notas_disponiveis_internas)}')
                # print(notas_disponiveis_internas)
                dinheiro_a_ser_levantado = lista[op]
            elif op < len(notas_disponiveis_internas) and len(notas_disponiveis_internas) > 0:
                # print(notas_disponiveis_internas)
                # print(f'LEN_: {len(notas_disponiveis_internas)}')
                dinheiro_a_ser_levantado = int(input(f'Que quantia desejas levantar?'
                                                     f' [entre 10€ e {notas_disponiveis_mostrar[-1]}]: '))
                temp = str(dinheiro_a_ser_levantado)

                if temp[-1] in '123456789' or dinheiro_a_ser_levantado < 10 or dinheiro_a_ser_levantado > notas_disponiveis_mostrar[-1]:
                    teste = False
                    while not teste:
                        if temp[-1] in '123456789':
                            if temp[-1] in '12':
                                print(f'\033[33mNão existem moedas de {temp[-1]}€'
                                      f' disponíveis no multibanco. Selecione apenas múltiplos de 10\033[m')
                            elif temp[-1] == '5':
                                print(f'\033[33mNão existem notas de {temp[-1]}€'
                                      f' disponíveis no multibanco. Selecione apenas múltiplos de 10\033[m')
                            else:
                                print(f'\033[33mNão é possível lenvantar valores cujo'
                                      f' o último algarismo seja {temp[-1]}€. Selecione apenas múltiplos de 10\033[m')
                        else:
                            print(f'\033[31mERRO! Por favor digita quantias apenas entre 10'
                                  f'€ e {notas_disponiveis_mostrar[-1]}€\033[m')
                        dinheiro_a_ser_levantado = int(input(f'Que quantia desejas levantar?'
                                                             f' [entre 10€ e {notas_disponiveis_mostrar[-1]}€]: '))
                        temp = str(dinheiro_a_ser_levantado)

                        if dinheiro_a_ser_levantado >= 10 and dinheiro_a_ser_levantado\
                                <= notas_disponiveis_mostrar[-1] and temp[-1] not in '123456789':
                            teste = True

            elif op == len(notas_disponiveis_internas):
                dinheiro_a_ser_levantado = - 1
                print()
                print('$ - '*15)
                print()
                if dados[3][0] != []:
                    for c in range(0, len(dados[3][0])):
                        print(f'Levantaste {dados[3][0][c]}€')
                else:
                    print()
                    print('Ainda não efetuaste nenhum levantamento')
                    print()

                    return dinheiro_a_ser_levantado

                print()
                print()
                print('$ - '*15)
                print()
            return dinheiro_a_ser_levantado
    else:
          dinheiro_a_ser_levantado = - 1
          print()
          print('$ - '*15)
          print()
          if dados[3][0] != []:
              for c in range(0, len(dados[3][0])):
                  print(f'Levantas-te {dados[3][0][c]}€')
          else:
              print('Ainda não efetuaste nenhum levantamento')
              print()

              return dinheiro_a_ser_levantado
          
          print()
          print('$ - '*15)
          print()
          return dinheiro_a_ser_levantado


def dispensador_de_notas(op, lista):
    notas_utilizadas_tipo_copia = notas_utilizadas_tipo.copy()
    notas_utilizadas_quant_copia = notas_utilizadas_quant.copy()


    temp = op
    # print(temp)
    cont = 0
    dinheiro_total = 0

    for c in range(len(notas_disponiveis)-1, -1, -1):
        cont = 0
        nota_atual = notas_disponiveis[c]
        quant_nota_atual = quant_notas_disponiveis[c]

        if op - nota_atual >= 0 and quant_nota_atual > 0:
            notas_utilizadas_tipo.append(nota_atual)
            notas_utilizadas_tipo_copia.append(nota_atual)
            while op - nota_atual >= 0:
                op -= nota_atual
                quant_notas_disponiveis[c] -= 1
                cont += 1
                dinheiro_total += nota_atual
            notas_utilizadas_quant_copia.append(cont)
            notas_utilizadas_quant.append(cont)
    dados[3][0].append(dinheiro_total)

    # print(dados)
    
    sleep(0.3)

    print()
    print(f'A levantar {temp}€...')
    print()
    # print(notas_utilizadas_quant_copia)
    # print(notas_utilizadas_tipo_copia)
    for i in range(0, len(notas_utilizadas_tipo_copia)):
        if notas_utilizadas_quant_copia[i] != 0:
            print(f'{notas_utilizadas_quant_copia[i]} notas de {notas_utilizadas_tipo_copia[i]}')

    notas_utilizadas_tipo_copia.clear()
    notas_utilizadas_quant_copia.clear()
    notas_utilizadas_tipo.clear()
    notas_utilizadas_quant.clear()


def recontador_de_notas(banco_0, banco_1):
    print()
    print('-'*30)
    for c in range(0, len(banco_0)):
        print(f'Existem {banco_0[c]} notas de {banco_1[c]}')
    print('-'*30)
    print()


def queres_continuar(tipo=0):
    if tipo == 0:
        resp = str(input('Queres continuar? [S/N]: ')).upper()

        if resp not in 'SN':
            while resp not in 'SN':
                print('\033[31mERRO! Opção inválida\033[m')
                resp = str(input('Queres continuar? [S/N]: ')).upper()
        if resp == 'S':
            return True
        else:
            return False
    else:
        resp = str(input('Terminar programa? [S/N]: : ')).upper()
        if resp not in 'SN':
            while resp not in 'SN':
                print('\033[31mERRO! Opção inválida\033[m')
                resp = str(input('Terminar Programa? [S/N]: ')).upper()
        if resp == 'S':
            return True
        else:
            return False


def verificar_legalidade_da_operacao(d, lista):
    lista_verificacao = []
    # print(f'OK {banco_de_dados}')
    # print(d)
    if d != -1:
        lista[2] += d
        # print(f'OK1 {banco_de_dados}')
        # print(f'OK1 {dados}')
        if lista[2] <= 400 and d <= 200:
            return True


banco_de_dados = [['utilizador1', 1234, 0 , [[], []]], ['utilizador2', 5678, 0, [[], []]],
                  ['utilizador3', 8765, 0, [[], []]], ['utilizador4', 4321, 0, [[], []]],
                  ['utilizador5', 1234, 0, [[], []]], ['utilizador6', 5678, 0, [[], []]],
                  ['utilizador7', 4321, 0, [[], []]]]
notas_disponiveis = [10, 20, 50, 100, 200]
quant_notas_disponiveis = [200, 100, 40, 20, 10]
notas_utilizadas_tipo = []
notas_utilizadas_quant = []
notas_disponiveis_internas = []


while True:
    utilizador = utilizador_existe(banco_de_dados)
    password = int(input('Password: '))
    pass_correta(utilizador, password, banco_de_dados)
    dados = retornar_os_dados_do_utilizador(utilizador, banco_de_dados)
    primeira_inicializacao_do_multibanco()
    while True:
        if dados[2] == 0:
            possibilidade_de_opcoes = inicializar_o_multibanco(0, 0, 0)
        elif 0 < dados[2] < 200:
            possibilidade_de_opcoes = inicializar_o_multibanco(0, 0, 1)
        else:
            possibilidade_de_opcoes = inicializar_o_multibanco(1, dados[2], 1)
        opcao = verificacao_da_opcao_de_levantamento(possibilidade_de_opcoes)
        dinheiro = opcao_de_levantamento(opcao, notas_disponiveis, possibilidade_de_opcoes)

        verificacao = verificar_legalidade_da_operacao(dinheiro, dados)
        if verificacao:
            dispensador_de_notas(dinheiro, dados)
            recontador_de_notas(quant_notas_disponiveis, notas_disponiveis)
            
        resp = queres_continuar()

        if not resp:
            break
    terminar_programa = queres_continuar(1)

    if terminar_programa:
        break




















