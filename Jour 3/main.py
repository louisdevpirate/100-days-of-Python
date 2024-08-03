import random

def randomize():
    return random.randint(1, 100)


result = randomize()

game = True

while game:
    try:
        guess = int(input("Choisis un nombre entre 1 et 100 : "))
        if guess > result:
            print("Trop haut !")
        elif guess < result:
            print("Trop bas !")
        elif guess == result:
            print("Bien joué ma poule !")
            game = False

    except ValueError:
        print("Vous devez rentrer un nombre entier compris entre 1 et 100")


