def eratosthene(n):
    premiers = [True] * (n + 1)
    premiers[0] = premiers[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if premiers[i]:
            for j in range(i * i, n + 1, i):
                premiers[j] = False

    return [i for i in range(2, n + 1) if premiers[i]]


print("Bienvenue au jeu des entiers d'Ératosthène ! Waouh ça va être super fun et pas du tout un truc de GROS NERD !!")
print()
print(
    "Bon tu vas commencer par me donner un nombre entier, et grâce à mon intelligence incomparable (et un programme informatique), je \nvais trouver tous les nombres premiers jusqu'au nombre que tu as entré.")
print("Si tu ne sais pas ce qu'est un nombre entier, regarde sur internet, je suis pas professeur de maths.")
print("Tu es prêt ?...")
print("Qu'est ce que je raconte moi...Bien sûr que tu es prêt. C'est pas un match de boxe, tu vas t'en sortir.")

while True:
    try:
        number = int(input("Allez, balance-moi un nombre entier (et positif, on n'est pas chez les barbares) : "))
        if number <= 0:
            print("Hé ho, j'ai dit POSITIF ! On recommence, champion.")
        elif number > 1000000:
            print(
                "Wow, doucement ! Je suis un assistant virtuel, pas un superordinateur. Essaie avec un nombre plus petit.")
        else:
            break
    except ValueError:
        print("Un nombre entier, c'est pas compliqué pourtant ! Allez, on se concentre et on réessaie.")

print(f"\nAttention, voici le moment que tout le monde attendait (ou pas)...")
print("Roulement de tambours...")
resultat = eratosthene(number)
print(f"Tadaaa ! Les nombres premiers jusqu'à {number} sont : {resultat}")
print("\nAlors, impressionné(e) ? Non ? Bon, tant pis, au moins on a appris quelque chose aujourd'hui. Peut-être.")