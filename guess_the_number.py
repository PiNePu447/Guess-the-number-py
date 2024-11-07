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
    
def greater(rhs, lhs):
    if rhs > lhs:
        print("é maior que isso")
    else:
        print("é menor que isso")

trys = 1

answer = None

while trys < 5 and answer != picked:
    answer = int(input("Coloque um numerdo de 1-100:\n-"))

    if answer == picked:
        print("Acertou em", trys, "tentativas")
    elif trys == 1:
        'print("Par:", isEven(picked), "Div5:", isDiv5(picked))'
        print("Par:", isEven(picked), "Div5:", isDiv5(picked))
        greater(picked, answer)
    else:
        greater(picked, answer)

    trys += 1