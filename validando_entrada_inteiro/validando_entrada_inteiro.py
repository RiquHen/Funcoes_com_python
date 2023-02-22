"""Função leia_int(), que vai funcionar de forma semelhante
'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')"""
def leia_int(msg):
    """
    ==> Validação de número inteiro
    :param msg: pede que seja informado um numero inteiro
    :return: imprime se o caracter digitado é um número inteiro
    """
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            return valor
            break
        else:
            print("\033[0;31mERRO! Digite um número inteiro válido.\033[0;0m")
        if ok:
            break


n = leia_int("Digite um número inteiro: ")
print(f"Você acabou de digitar o número {n}.\n{50*'='}")
help(leia_int)
