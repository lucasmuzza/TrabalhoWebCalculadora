# Arquivo com funções matemáticas

def calcular_soma(a, b):
    return a + b

def calcular_subtracao(a, b):
    return a - b


def calcular_multiplicao(a, b):
    return a * b

def calcular_divisao(a, b):
    if b == 0:
        raise ValueError("Não é possível realizar divisão por zero.")
    return a / b
