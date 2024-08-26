import random


def create_list():
    random_list = []
    for _ in range(20):
        random_list.append(random.randint(0, 100))
    return random_list


def number_to_search():
    while True:
        try:
            nombre_a_chercher = int(input("Veuillez entrer un nombre (entier) à chercher dans la liste : "))
            return nombre_a_chercher
        except ValueError:
            print("Non c'est pas bon, ce n'est pas un nombre entier")


def binary_search(list, input):
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
    while True:
        response = input("Voulez-vous faire une nouvelle recherche ? (oui/non) : ").lower().strip()
        if response in ['oui', 'non']:
            return response == 'oui'
        print("Veuillez répondre par 'oui' ou 'non'.")


def main():
    while True:
        liste = create_list()
        liste.sort()
        print("Liste générée et triée :", liste)

        nombre = number_to_search()
        resultat = binary_search(liste, nombre)

        if resultat != -1:
            print(f"Le nombre {nombre} a été trouvé à l'index {resultat}")
        else:
            print(f"Le nombre {nombre} n'est pas dans la liste")

        if not ask_continue():
            print("Merci d'avoir utilisé ce programme. Au revoir !")
            break


if __name__ == "__main__":
    main()