import os
from time import sleep

# listas com os valores por extenso, a cada operação em busca do digito[milhar, centena, dezena e unidades] o valor é buscado na lista, de acordo com cada funcao
unidades = ["zero", "um", "dois", "três", "quatro",
            "cinco", "seis", "sete", "oito", "nove"]
teens = ['dez', "onze", "doze", "treze", "quatorze", "quinze",
         "dezesseis", "dezessete", "dezoito", "dezenove"]
tens = ["dez", "vinte", "trinta", "quarenta", "cinquenta",
        "sessenta", "setenta", "oitenta", "noventa"]
cents = ["cem", "cento", 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
         'seiscentos', 'setecentos', 'oitocentos', 'novecentos']
milhar = ['mil', 'dois mil ', 'três mil', 'quatro mil', 'cinco mil', 'seis mil',
          'sete mil', 'oito mil', 'nove mil']

# Função usada para exibir o titulo do programa


def titulo():
    print(f"{'-'*50}\n{'Número Por Extenso':^50}\n{'-'*50}")


def mil(num):
    """ Verifica se valor(num) é da casa dos milhares, em caso positivo busca a string na lista 'milhar', implementada no inicio do programa
    Args:
        num (int): informado pelo usuário
    Returns:
        string:  retornando a string com o valor da milhar por extenso: mil([num//1000])
    """
    m = num // 1000
    r = num % 1000
    if r > 0:
        return f'{milhar[m-1]} e '
    else:
        return f'{milhar[m-1]}'


def cem(num):
    """testa se o digito na casa das centenas é diferente de zero
    Args:
        num (int): informado pelo usuário, ou resto no caso do numero informado ser maior que 999
    Returns:
        string: retorna string com o valor da centena por extenso, cents[num//100-1]
    """
    c = num // 100
    r = num % 100
    if r == 0:
        if c == 1:
            return f'{cents[c-1]}'
        else:
            return f'{cents[c]}'
    elif r > 0:
        return f'{cents[c]} e '
    else:
        return f'{cents[c]}'


def dez(num):
    """testa se o digito na casa das dezenas é diferente de zero
    Args:
        num (int): informado pelo usuário, ou resto no caso do numero informado ser maior que 99
    Returns:
        _type_: retorna a string com o valor da dezena por extenso, caso resto de num%10 = 0 pega a string em tens[(num//10) - 1], e se for diferente teens[num%10] ou teens[resto]
    """
    d = num // 10
    r = num % 10
    if r == 0:
        return f'{tens[d-1]}'
    else:
        if d == 1:
            return f'{teens[r]}'
        else:
            return f'{tens[d-1]} e '


def continua():
    """ Verifa se o  usuário deseja contunuar lendo os numeros por extenso
    Returns:
        bool: de acordocom o valor  que o usuario enviar.(False ou True)
    """
    continua = input('Continua?[s ou n]').strip()[0]
    if continua in 'nN':
        print('Saindo...')
        sleep(2)
        print('Até a próxima!!!')
        return False
    else:
        return True


def teste_num(numero):
    """Verifica se o numero informado é inteiro e está entre 0 e 9999
    Args:
        numero (int):informado pelo usuario
    Returns:
        int: após a verificação do numero ser válida
    """
    try:
        if 9999 >= numero:
            return numero
        else:  # executa se Caso o numero digitado seja inteiro e maior que 9999 ou menor que 0
            print('0Por favor, apenas números entre 0 e 9999.')
    except:  # excuta se caso o valor informado naoseja um numero inteiro
        print('Por favor!!! Apenas números inteiros, entre 0 e 9999.')

# testa o numero e imprime a saida completa do numero por extenso, trata inclusive quando a saida do valor do digito das unidades deve ser adicionado a string[saida - numero por extenso]


def por_extenso(num):
    sleep(3)
    os.system('cls')
    titulo()
    """help(mil)
    help(cem)
    help(dez)"""

    saida = ''
    print(num, end=' = ')
    # executa se o numero estive na casa do milhar[4º digito diferente de zero]
    if 9999 >= num > 999:
        saida += mil(num)
        num %= 1000
    # executa se o numero tiver cada de centenas[3º digito digerente de zero]
    if 999 >= num > 99:
        saida += cem(num)
        num %= 100
    # executa se o numero da dezena for diferente de zero
    if 99 >= num > 9:
        saida += dez(num)
    #  executa se ultimo digito for diferente de zero e digito da dezena for diferente de 1 e no caso de os outros 3 digitos forem igual a zero
    if num % 10 != 0 and num // 10 != 1 or saida == '':
        saida += unidades[num % 10]
    print(f'{saida}\n{"-"*50}')

titulo()
while True:
    try:
        numero = int(input('Informe um número inteiro(entre 0 e 9999): '))
        if numero <= 9999:
            por_extenso(numero)
            if not continua():
                break
    except:  # excuta se caso o valor informado naoseja um numero inteiro
        print(f'\033[1;31mPor favor!!! Apenas números inteiros, entre 0 e 9999.\033[0;0m')
    else:  # executa se Caso o numero digitado seja inteiro e maior que 9999 ou menor que 0
        print(f'\033[1;31mPor favor, apenas inteiros entre 0 e 9999.\033[0;0m')
