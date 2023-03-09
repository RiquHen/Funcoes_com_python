"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com escrevaanho adaptável."""
import os

def escreva(frase):
    t = int(len(frase)+4)
    print(f"{t*'='}\n{frase.center(t)}\n{t*'='}")


escreva("Informe a frase para colocá entre os separadores de tmaanho adptável")

frase = input('Informe a frase: ')
os.system('cls')
escreva(frase)
