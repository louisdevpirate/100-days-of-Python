def tri_a_bulles(liste):
    n = len(liste)
    echange = True
    while echange:
        echange = False
        for i in range(n - 1):
            if liste[i] > liste[i + 1]:
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                echange = True
    return liste


def obtenir_liste():
    while True:
        try:
            entree = input("Entrez plusieurs nombres entiers, séparés par des virgules : ")
            # Divise l'entrée en une liste de chaînes, puis convertit chaque chaîne en entier
            ma_liste = [int(x.strip()) for x in entree.split(',')]
            return ma_liste
        except ValueError:
            print("\nErreur : Veuillez entrer uniquement des nombres entiers séparés par des virgules.\n")


# Obtenir la liste de l'utilisateur
ma_liste = obtenir_liste()

print("\nListe non triée:", ma_liste)
liste_triee = tri_a_bulles(ma_liste)
print("\nListe triée:", liste_triee)