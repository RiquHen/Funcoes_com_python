"""Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com escrevaanho adaptável."""

def escreva(frase):
    t = int(len(frase)+4)
    print(f"{t*'='}\n{frase.center(t)}\n{t*'='}")


escreva("Assim será de novo")
escreva("Bom dia, senhoras e senhores!!!")
escreva("Função com mensagem de tamanho de separador adaptável")
escreva("abc")
