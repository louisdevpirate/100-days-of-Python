import random

# Fonction qui génère un nombre entier aléatoire entre 1 et 100
def randomize():
    return random.randint(1, 100)

# Nombre aléatoire contenu dans la variable result
result = randomize()

# Préparation de la boucle While et création des tentatives
attempts = 0
# Attribution du nombre maximum de tentatives
max_attempts= 20

# Message de bienvenue
print("\nBienvenue dans le jeu de euh...deviner le nombre entre 1 et 100 ! Cool non ? Bon alors voici les règles : \n...\nEst ce que j'ai vraiment besoin de t'expliquer les règles de ce jeu ? Sérieusement ?\n\nBon aller, sans plus attendre, commençons !\n")

# Le jeu s'arrête une fois la bonne réponse trouvée ou quand plus de tentatives restantes
while attempts < max_attempts :
    try:
        guess = int(input("Choisis un nombre entre 1 et 100 : "))

        # Gère le cas où l'utilisateur rentre un nombre qui ne soit pas compris entre 1 et 100
        if guess > 100 or guess < 1:
            print("Entre 1 et 100 on t'a dit !")

        elif guess > result:
            print("\nTROP HAUT !")
            attempts += 1
            print(f"Plus que {10-attempts} chances !\n")

        elif guess < result:
            print("\nTROP BAS !")
            attempts += 1
            print(f"Plus que {10 - attempts} chances !\n")

        # Message de victoire pour le joueur
        elif guess == result:
            print(f"\nBien joué. T'es trop fort, tu as trouvé en {attempts} tentatives ! \n(J'aurais sûrement fait mieux...mais bravo à toi !)")
            break

        # Message d'échec quand l'utilisateur a cramé toutes ses tentatives
        elif attempts == 10:
            print("BOOOOUH ! Gros Loser ! Ça fait quoi de pas réussir à trouver un nombre entier entre 1 et 100, tu sais lacer tes chaussures au moins ?\nBon...c'est pas grave...tu veux retenter ta chance ?")

    # Message d'erreur quand l'utilisateur ne rentre pas un nombre entier
    except ValueError:
        print("\nUn NOMBRE, tu dois rentrer un nombre bordel !\n")


