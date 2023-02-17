# Programa escolhe um numero aleatório que
# deverá ser descoberto pelo usário

from random import randint
import os
from time import sleep

# insere uma pequena introdução, no inicio de toda rodada.(inicio do jogo e caso continue jogando)


def titulo():
    os.system('cls')
    print(f"{'~'*50}\n{'MENTALISTA':^50}\n{'~'*50}")
    print('Escolherei um número entre 0 e 100,\n\tPor favor tente advinhá-lo.')
    print(f"Não se preocupe, dicas serão apresentadas\n{'~'*50}")

# verifica se o usuário deseja continuar a jogada [s ou n], caso seja negativo encerra o programa


def continuar():
    continua = input('Jogar novamente?[s ou n]').strip().lower()[0]
    if continua == 'n':
        sleep(2)
        os.system('cls')
        print('Obrigado por jogar comigo. \n\t\tAté a próxima!!!')
        return False
    else:
        titulo()
        return True
# verifica se o chute dado pelo jogador é igual ao numero sorteado


def acerto():
    sleep(1.3)
    # os.system('cls')
    print(
        f'\n\033[1;34m{"~"*50}\n~~~~~ PARABENS VOCÊ ACERTOU!!! ~~~~~')
# inicio das variáveis utilizadas, maximo e minimo(dicas), sorteio e zera o numero de tentativas


def inicio():
    sorteio = randint(1, 100)  # numero aleatório escolhido
    minimo = tentativas = 0  # minimo - valor minimo para chute
    maximo = 100  # valor maximo para chute
    return sorteio, minimo, maximo, tentativas

# de acordo com o chutado numero,verifica as dicas, valores maximo e minimo


def verifica_min_max(chute, sorteio, minimo, maximo, tentativas):
    sleep(1.3)
    if chute < minimo or chute > maximo:
        print(
            f'\033[1;31mChute Inválido!!!\nApenas número entre {minimo} a {maximo}!!!\033[0;0m ')
    elif chute < sorteio and chute > minimo:
        minimo = chute
        print(f'{"Tente novamente"}\n{"~"*30}')
    elif chute > sorteio and chute < maximo:
        maximo = chute
        print(f'{"Tente novamente"}\n{"~"*30}')
    return minimo, maximo, tentativas


def main():
    sorteio, minimo, maximo, tentativas = inicio()
    while True:
        try:
            print('Informe seu palpite...', end='')
            chute = int(input(f'{minimo} a {maximo}: '))
            tentativas += 1
            if chute == sorteio:
                acerto()
                print(
                    f'\nForam necessárias: {tentativas} tentativas\n{"~"*50}\033[0;0m')
                sorteio, minimo, maximo, tentativas = inicio()
                if not continuar():
                    break
                os.system('cls')
            else:
                # verifica_min_max(chute, sorteio, minimo, maximo, tentativas)
                minimo, maximo, tentativas = verifica_min_max(
                    chute, sorteio, minimo, maximo, tentativas)
        except:
            print(
                f'\033[1;33mInforme um numero inteiro entre {minimo} e {maximo}\033[0m')


# Inicio da execução do jogo -- Mentalista --
titulo()
jogar = input('pressione enter para iniciar[ n - SAIR]').lower()
if jogar == 'n':
    print(
        f'\033[1;33m{"="*50}\nEntão OK, fica para próxima!!!\nb{"="*50}\033[0;0m')
else:
    main()
