def tri_a_bulles(liste):
    n = len(liste)
    echange = True

    # Continue jusqu'à ce qu'aucun échange ne soit fait
    while echange:
        echange = False
        # Parcourt la liste jusqu'à l'avant-dernier élément
        for i in range(n - 1):
            # Compare l'élément actuel avec le suivant
            if liste[i] > liste[i + 1]:
                # Échange les éléments si ils sont dans le mauvais ordre
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                # Indique qu'un échange a eu lieu
                echange = True

    return liste


# Exemple d'utilisation
ma_liste = [64, 34, 25, 12, 22, 11, 90]
print("Liste non triée:", ma_liste)
liste_triee = tri_a_bulles(ma_liste)
print("Liste triée:", liste_triee)