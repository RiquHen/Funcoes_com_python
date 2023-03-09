"""Faça um programa, com uma função que necessite de três argumentos,
e que forneça a soma desses três argumentos."""
def soma(x, y):
    return x+y

def subtracao(x,y):
    return x - y

def multiplicacao(x,y):
    return x*y

def divisao(x,y):
    return x/y

numero_1 = float(input('Informe o primeiro número: '))
numero_2 = float(input('Informe o segundo número: '))
print(f'adição: {soma(numero_1,numero_2)}')
print(f'subtração: {subtracao(numero_1,numero_2)}')
print(f'multiplicação: {multiplicacao(numero_1,numero_2)}')
print(f'divisão: {divisao(numero_1,numero_2)}')