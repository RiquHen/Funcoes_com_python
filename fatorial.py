""" Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""
import os


def fatorial(n, show=False):
    """
    ==> Calcula o fatorial de um número informado
    :param n: número informado para se calcular o fatorial
    :param show = True mostra todos os números usados no calculo do Fatorial
    :return :  fatorial de um número informado pelo usuário:
    """
    fat = 1
    for i in range(n, 0, -1):
        if show:
            if i == 1:
                print(f"{i}", end=" = ")
            else:
                print(f"{i}", end=" x ")
        fat *= i
    return fat

os.system('cls')
num= int(input("Deseja saber o fatorial de: "))
print(f"{15 * '=-'}\nSHOW = True")
print(f"{fatorial(num, show=True)}")
print(f"{15 * '=-'}\nFatorial de {num}: {fatorial(num)}\n{15 * '=-'}")