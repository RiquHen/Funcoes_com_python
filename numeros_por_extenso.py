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

# testa se há digito diferente de zero na casa dos milhar retornando a string com o valor por extenso
def mil(num):
    m = num // 1000
    r = num % 1000
    if r > 0:
        return f'{milhar[m-1]} e '
    else:
        return f'{milhar[m-1]}'

# testa se o digito na casa das centenas é diferente de zero e retornando a string com o valor por extenso
def cem(num):
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

# testa se o digito na casa das dezenas é diferente de zero e retornando a string com o valor por extenso
def dez(num):
    d = num // 10
    r = num % 10
    if r == 0:
        return f'{tens[d-1]}'
    else:
        if d == 1:
            return f'{teens[r]}'
        else:
            return f'{tens[d-1]} e '

# testa o numero e imprime a saida completa do numero por extenso, trata inclusive quando a saida do valor do digito das unidades deve ser adicionado a string[saida - numero por extenso]
def por_extenso(num):
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
    print(saida)


while True:
    sleep(3)
    os.system('cls')
    titulo()
    try:
        numero = int(input('Informe um número inteiro(entre 0 e 9999): '))
        if 9999 >= numero:
            por_extenso(numero)
            continua = input('Continua?[s ou n]').strip()[0]
            if continua in 'nN':
                print('Saindo...')
                sleep(2)
                print('Até a próxima!!!')
                break
        else:
            print('Por favor, apenas números entre 0 e 9999.')
    except:
        print('Por favor!!! Apenas números inteiros, entre 0 e 9999.')
