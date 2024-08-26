# fonction recherche_binaire(liste, element_recherche):
# debut = 0
# fin = longueur
# de
# la
# liste - 1
#
# tant
# que
# debut <= fin:
# milieu = (debut + fin) // 2
# if liste[milieu] == element_recherche:
#     return milieu  # Élément trouvé
# elif liste[milieu] < element_recherche:
#     debut = milieu + 1
# else:
#     fin = milieu - 1
#
# return -1  # Élément non trouvé

def binary_search(list, input):
    start = 0
    end = len(list) - 1

    while start <= end:
        middle = (start + end) // 2
        if list[middle] == input:
            print("Trouvé !")
            return middle
        elif list[middle] < input:
            start = middle + 1
        else:
            end = middle - 1

    print("Nombre introuvable")
    return -1


liste = [2, 4, 7, 9, 10, 12, 13, 14, 15, 18, 56]
nombre_a_chercher = 16

binary_search(liste, nombre_a_chercher)
