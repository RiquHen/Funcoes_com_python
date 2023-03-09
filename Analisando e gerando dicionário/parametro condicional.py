"""Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações: total de notas, media, maior e menor nota, situação se paramentro for True"""
import os

def notas(*n, sit=False):
    """
    ==> Função que analisa notas, média e situação de vários alunos
    :param n: uma ou mais notas dos alunos(aceitando várias notas)
    :param sit: valor opcional que indica  se deve ou não adicionar a situação
    :return: dicionário com  várias informações sobre o aluno ou turma
    """
    resumo = dict()
    situa = ""
    resumo["total"] = len(n)
    resumo["media"] = sum(n)/len(n)
    resumo["Maior"] = max(n)
    resumo["Menor"] = min(n)
    if sit:
        if sum(n)/len(n) < 5:  # pode ser tambem resumo["media"]/ resumo["total"]
            resumo["situacao"] = "RUIM"
        elif sum(n)/len(n) > 7:  # pode ser tambem resumo["media"]/ resumo["total"]
            resumo["situacao"] = "BOA"
        else:
            resumo["situacao"] = "REGULAR"

    return resumo


os.system('cls')
print(notas(5, 3, 4, 8))
print(notas(6, 3, 8, 9, 2, sit=True))
print()
#help(notas)