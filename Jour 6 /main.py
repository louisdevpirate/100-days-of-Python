def addition(first_number, second_number):
    return first_number + second_number


def soustraction(first_number, second_number):
    return first_number - second_number


def multiplication(first_number, second_number):
    return first_number * second_number


def division(first_number, second_number):
    if second_number == 0:
        return "Division par 0 impossible."
    return first_number / second_number


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")


operations = {
    "addition": addition,
    "soustraction": soustraction,
    "division": division,
    "multiplication": multiplication
}


while True:
    operation = input("\nQuelle opération souhaitez-vous effectuer ? Addition/Soustraction/Multiplication/Division\nEntrez votre réponse ici : ").lower()

    if operation in operations:
        number1 = get_number("\nChoisissez un premier nombre : ")
        number2 = get_number("\nChoisissez un deuxième nombre : ")

        result = operations[operation](number1, number2)
        print(f"\nLe résultat est {result}")

        if input("\nVoulez vous exécuter un autre calcul ? Oui/Non : ").lower() != 'oui':
            break

    else:
        print("\nOpération non valide. Veuillez réessayer.\n")





