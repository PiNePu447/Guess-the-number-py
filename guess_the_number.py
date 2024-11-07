import random

numbers = range(1, 100)

picked = random.choice(numbers)

def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

def isDiv5(number):
    if number % 5 == 0:
        return True
    else:
        return False
    
def maiorMenor(rhs, lhs):
    if rhs > lhs:
        print("é maior que isso")
    else:
        print("é menor que isso")

tentativas = 1

resposta = None

while tentativas < 5 and resposta != picked:
    resposta = int(input())

    if resposta == picked:
        print("Acertou em", tentativas, "tentativas")
    elif tentativas == 1:
        'print("Par:", isEven(picked), "Div5:", isDiv5(picked))'
        print("Par:", picked % 2 == 0, "Div5:", picked%5==0)
        maiorMenor(picked, resposta)
    else:
        maiorMenor(picked, resposta)

    tentativas += 1