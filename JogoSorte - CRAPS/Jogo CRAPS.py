"""Jogo de Craps. Faça um programa de implemente um jogo de Craps.
O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada,
você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. 
Se na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,
este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente."""

from random import randint
from time import sleep
import os

def regras():
    """se tirar 7 ou 11 na primeiro sorteio, você um "NATURAL" e você GANHA.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "CRAPS" e você PERDE. 
Se na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "PONTO". 
Jogadas seguem, se tirar 7-PERDE, se tirar o valor igual ao PONTO, você VENCE.
    """
def titulo(msg):
    """ inicio da rodada - cabeçalho
    Args:
        msg (_type_): argumento impresso entre duas linhas
    """
    print(f"{'-'*70}\n{msg:^60}\n{'='*70}")


def jogada():
    """ Sorteia dois numeros inteiro
    Returns:
        _type_: retorna a soma de dois numeros inteiros sorteados
    """
    sleep(1.5)
    resul = 0
    resul = randint(1, 6) + randint(1, 6)
    return resul


def continuar():
    """ Verifica se o usuário deseja continuar a jogar
    Returns:
        _type_: retorno booleano, que faz com que o laço while do jogo return True ou encerre
    """
    continua = input('Jogar mais 1 vez? [n - SAIR] ').strip().lower()
    if continua == 'n':
        return False
    else:
        os.system('cls')
        return True


def main():
    global cont, ponto, res, vit, der
    cont += 1
    res = jogada()

    print(f"PONTO:  {ponto} --- JOGADA: {res}\n{'-' * 30}")
    sleep(1)
    if cont == 1:
        ponto = res
        if res == 2 or res == 3 or res == 12:
            titulo(f"{res} - Você fez um Craps... Você PERDEU!!!")
            der += 1
            if continuar():
                titulo("INICIANDO UMA PARTIDA DE CRAPS")
                cont = ponto = 0
                return True
            else:
                return False
        elif res == 7 or res == 11:
            titulo(
                f"{res} - GANHOUUU !!!! Você é um natural... Você Ganhou. Parabéns!!!")
            vit += 1
            if continuar():
                titulo("INICIANDO UMA PARTIDA DE CRAPS")
                cont = ponto = 0
                return True
            else:
                return False
        elif res == 4 or res == 5 or res == 6 or res == 8 or res == 9 or res == 10:
            ponto = res
            return True
            
    elif cont > 1:
        if res == 7:
            titulo(
                f"{res} - Você PERDEU tirou {res} antes de acertar o ponto {ponto}!")
            der += 1
            if continuar():
                cont = ponto = 0
                titulo("INICIANDO UMA PARTIDA DE CRAPS")
                return True
            else:
                return False
        elif res == ponto:
            titulo(f"{res} - GANHOUUUU!!! Parabéns... Você Ganhou!!!")
            vit += 1
            if not continuar():
                return False
            else:
                cont = ponto = 0
                titulo("INICIANDO UMA PARTIDA DE CRAPS")
                return True
        else:
            return True
"""help(jogada)
help(continuar)
help(titulo)"""

cont = ponto = vit = der = 0
titulo('JOGO DE SORTE - "CRAPS"')
while True:
    try:
        regra = int(input('1 - Regras     2 - Jogar\t'))
        if regra == 1:
            help(regras)
            continue
    except:
        print('\033[1;31mOpção Invalida!!! 1 - Regras  --  2 - Jogar\033[0;0m')
    else:
        os.system('cls')
        break

titulo('Iniciando uma Partida de "CRAPS"')
while True:
    if not main():
        sleep(1.4)
        print(f'{"-"*70}\nVocê ganhou: {vit}\nVocê perdeu: {der}\n{"-"*70}')
        print(f'Saindo do Jogo...\n\t\tAté a próxima!!!')
        break