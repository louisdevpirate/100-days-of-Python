def addition(first_number, second_number):
    result = first_number + second_number
    print(f"Le résultat est : {result}")


def soustraction(first_number, second_number):
    result = first_number - second_number
    print(f"Le résultat est : {result}")


def division(first_number, second_number):
    result = first_number / second_number
    print(f"Le résultat est : {result}")


def multiplication(first_number, second_number):
    result = first_number * second_number
    print(f"Le résultat est : {result}")


operation = input("Quelle opération souhaitez vous effectuer ? Addition/Soustraction/Multiplication/Division\nEntrez votre réponse ici : ")
answer = operation.lower()
number1 = int(input("Choisissez un premier nombre : "))
number2 = int(input("Choisissez un deuxièpme nombre : "))


if answer == "addition":
    addition(number1, number2)

if answer == "soustraction":
    soustraction(number1, number2)

if answer == "multiplication":
    multiplication(number1, number2)

if answer == "division":
    division(number1, number2)

