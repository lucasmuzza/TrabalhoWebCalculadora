# Arquivo com funções matemáticas

def calcular_soma(a, b):
    return a + b

def calcular_subtracao(a, b):
    return a - b


def calcular_multiplicao(a, b):
    return a * b

def calcular_divisao(a, b):
    if a == 0 or b == 0:
        raise ValueError("Não é possível realizar divisões com 0.")
    
    return a / b
