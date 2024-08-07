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

while True:
    operation = input("Quelle opération souhaitez-vous effectuer ? Addition/Soustraction/Multiplication/Division\nEntrez votre réponse ici : ").lower()
    if operation in ["addition", "soustraction", "multiplication", "division"]:
        break
    else:
        print("Opération non valide. Veuillez réessayer.")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")


number1 = get_number("Choisissez un premier nombre : ")
number2 = get_number("Choisissez un deuxième nombre : ")
