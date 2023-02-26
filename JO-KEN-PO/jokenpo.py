from random import choice
from time import sleep

opcoes = ['pedra', 'papel', 'tesoura']

# formata a saida do programa, se ganhou, perdeu ou empate
def saida(msg):
    print(f'{msg:~^40}')

# testa as jogadas ... jogadas do pc usando choice() na lista opções
def teste(eu, pc):
    if eu == pc:
        saida('Empate')
    elif eu == 'pedra':
        if pc == 'papel':
            saida('Computador venceu!!!')
        elif pc == 'tesoura':
            saida('Parabéns Você Venceu!!!')
    elif eu == 'tesoura':
        if pc == 'papel':
            saida('Parabéns Você Venceu!!!')
        elif pc == 'pedra':
            saida('Computador Venceu!!!')
    elif eu == 'papel':
        if pc == 'pedra':
            saida('Parabéns Você Venceu!!!')
        elif pc == 'tesoura':
            saida('Computador Venceu!!!')


while True:
    sleep(2)
    print(f"{'='*40}\n{'JO-KEN-PO':^40}")
    try:
        jogada = int(
            input(f'{"="*40}\nFaça sua jogada...\n[1] - pedra\t[2] - papel \n[3] - tesoura\t[0] - SAIR\n\tJogada: '))
        print(f'{"="*40}')
        while jogada > 3:
            print('Opção Inválida!!! Somente número de 0 a 3 são opções.')
            jogada = int(input('Informe sua opção\n[1] - pedra\t[2] - papel \n[3] - tesoura\t\t[0] - SAIR\n\tJogada: '))
        jogada_pc = choice(opcoes)
        sleep(2)
        if jogada == 0:
            break
        elif jogada == 1:
            jogada = 'pedra'
            print(f'Você escolheu {jogada}!')
        elif jogada == 2:
            jogada = 'papel'
            print(f'Você escolheu {jogada}!')
        elif jogada == 3:
            jogada = 'tesoura'
            print(f'Você escolheu {jogada}!')
        print(f'O computador escolheu: {jogada_pc}')
        teste(jogada, jogada_pc)
        sleep(2)
    except:
        print('Opção Inválida!!!  Somente número de 0 a 3 são opções.')
