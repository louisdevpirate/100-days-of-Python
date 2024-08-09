def tri_a_bulles(liste):
    """
    Trie une liste en utilisant l'algorithme du tri à bulles.

    :param liste: La liste à trier
    :return: La liste triée (la même liste, modifiée sur place)
    """
    n = len(liste)
    echange = True
    while echange:
        echange = False
        for i in range(n - 1):
            # Si l'élément actuel est plus grand que le suivant, on les échange
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                echange = True
    return liste


def obtenir_liste():
    """
    Demande à l'utilisateur d'entrer une liste de nombres entiers.
    Gère les erreurs de saisie et continue à demander jusqu'à obtenir une entrée valide.

    :return: Une liste d'entiers saisie par l'utilisateur
    """
    while True:
        try:
            # Demande à l'utilisateur d'entrer des nombres
            entree = input("Entrez plusieurs nombres entiers, séparés par des virgules : ")

            # Divise l'entrée en une liste de chaînes, puis convertit chaque chaîne en entier
            ma_liste = [int(x.strip()) for x in entree.split(',')]

            # Si tout s'est bien passé, on retourne la liste
            return ma_liste
        except ValueError:
            # Si une erreur se produit (par exemple, si l'utilisateur entre des lettres),
            # on affiche un message d'erreur et on recommence la boucle
            print("Erreur : Veuillez entrer uniquement des nombres entiers séparés par des virgules.")


# Programme principal
# Obtenir la liste de l'utilisateur
ma_liste = obtenir_liste()

# Afficher la liste non triée
print("Liste non triée:", ma_liste)

# Trier la liste et afficher le résultat
liste_triee = tri_a_bulles(ma_liste)
print("Liste triée:", liste_triee)