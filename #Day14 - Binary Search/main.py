import random


def get_list_size():
    """
    Demande à l'utilisateur la taille de la liste à générer.

    Returns:
    int: La taille de la liste, entre 1 et 100.
    """
    while True:
        try:
            size = int(input("Entrez la taille de la liste (entre 1 et 100) : "))
            if 1 <= size <= 100:
                return size
            print("La taille doit être entre 1 et 100.")
        except ValueError:
            print("Veuillez entrer un nombre entier valide.")


def create_list(size):
    """
    Crée une liste triée de nombres aléatoires.

    Args:
    size (int): La taille de la liste à générer.

    Returns:
    list: Une liste triée de nombres aléatoires.
    """
    # Génère une liste de nombres aléatoires entre 0 et 100
    return sorted([random.randint(0, 100) for _ in range(size)])


def number_to_search():
    """
    Demande à l'utilisateur le nombre à rechercher.

    Returns:
    int: Le nombre à rechercher dans la liste.
    """
    while True:
        try:
            return int(input("Veuillez entrer un nombre (entier) à chercher dans la liste : "))
        except ValueError:
            print("Non c'est pas bon, ce n'est pas un nombre entier")


def binary_search(list, input):
    """
    Effectue une recherche binaire dans la liste.

    Args:
    list (list): La liste triée dans laquelle effectuer la recherche.
    input (int): Le nombre à rechercher.

    Returns:
    int: L'index du nombre trouvé, ou -1 si non trouvé.
    """
    start = 0
    end = len(list) - 1

    while start <= end:
        middle = (start + end) // 2
        if list[middle] == input:
            return middle
        elif list[middle] < input:
            start = middle + 1
        else:
            end = middle - 1

    return -1


def ask_continue():
    """
    Demande à l'utilisateur s'il souhaite continuer.

    Returns:
    bool: True si l'utilisateur souhaite continuer, False sinon.
    """
    while True:
        response = input("Voulez-vous faire une nouvelle recherche ? (oui/non) : ").lower().strip()
        if response in ['oui', 'non']:
            return response == 'oui'
        print("Veuillez répondre par 'oui' ou 'non'.")


def main():
    """
    Fonction principale qui gère le flux du programme.
    """
    while True:
        try:
            # Obtenir la taille de la liste et la créer
            list_size = get_list_size()
            liste = create_list(list_size)
            print("Liste générée et triée :", liste)

            # Demander le nombre à rechercher et effectuer la recherche
            nombre = number_to_search()
            resultat = binary_search(liste, nombre)

            # Afficher le résultat de la recherche
            if resultat != -1:
                print(f"Le nombre {nombre} a été trouvé à l'index {resultat}")
            else:
                print(f"Le nombre {nombre} n'est pas dans la liste")

            # Demander si l'utilisateur veut continuer
            if not ask_continue():
                print("Merci d'avoir utilisé ce programme. Au revoir !")
                break
        except Exception as e:
            # Gestion générale des exceptions
            print(f"Une erreur inattendue s'est produite : {e}")
            print("Le programme va redémarrer.")


if __name__ == "__main__":
    main()