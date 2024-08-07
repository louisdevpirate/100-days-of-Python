def addition(first_number, second_number):
    result = first_number + second_number
    print(f"Le résultat est : {result}")


def soustraction(first_number, second_number):
    result = first_number - second_number
    print(f"Le résultat est : {result}")


def division():
    while True:
        try:
            first_number = float(input("Entrez le premier nombre : "))
            second_number = float(input("Entrez le deuxième nombre : "))
            if second_number == 0:
                print("Division par 0 impossible. Veuillez entrer un diviseur non nul.")
                continue
            result = first_number / second_number
            print(f"Le résultat est : {result}")
            break
        except ValueError:
            print("Veuillez entrer des nombres valides.")


def multiplication(first_number, second_number):
    result = first_number * second_number
    print(f"Le résultat est : {result}")


while True:
    operation = input("Quelle opération souhaitez-vous effectuer ? Addition/Soustraction/Multiplication/Division\nEntrez votre réponse ici : ").lower()
    if operation in ["addition", "soustraction", "multiplication", "division"]:
        break
    else:
        print("\nOpération non valide. Veuillez réessayer.\n")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")


number1 = get_number("\nChoisissez un premier nombre : ")
number2 = get_number("\nChoisissez un deuxième nombre : ")
