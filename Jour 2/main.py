# Ecrivez une fonction qui prend une liste de nombre, et retourne une nouvelle liste qui ne contient que les nombres pairs

def ask_list():
    """
    Demande à l'utilisateur de saisir une liste de nombres séparés par des virgules,
    et retourne cette liste sous forme d'une liste d'entiers.
    """
    while True:
        try:
            saisie = input("Donnez une liste de nombres, séparés par une virgule : ")
            list_str = saisie.split(',')
            list_result = [int(nombres.strip()) for nombres in
                           list_str]  # Utilisation de strip() pour enlever les espaces
            return list_result
        except ValueError:
            print("Veuillez entrer des nombres valides, séparés par des virgules.")


def even_numbers(numbers):
    """
    Filtre une liste de nombres pour ne conserver que les nombres pairs.

    Paramètre:
    numbers (list): La liste des nombres à filtrer.

    Retourne:
    list: Une nouvelle liste contenant seulement les nombres pairs.
    """
    return [number for number in numbers if number % 2 == 0]


# Exemple d'utilisation
liste = ask_list()
print(f"Vous avez entré la liste suivante : {liste}")

even = even_numbers(liste)
print(f"Les nombres pairs de votre liste sont les suivants : {even}")
