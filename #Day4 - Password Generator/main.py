# #Day4 - Password Generator : Écrivez un programme qui génère un mot de passe aléatoire d'une longueur donnée, contenant des lettres majuscules, minuscules, des chiffres et des caractères spéciaux.
import random
import string

# Constantes pour valeur minimales et maximales
MIN_LENGTH = 12
MAX_LENGTH = 50

# Création d'une fonction qui génère une chaîne de caractères aléatoires (la longueur par défaut est 12)
def generate(longueur=MIN_LENGTH):
    # La longueur du mot de passe ne peut pas être inférieure à 12 caractères
    while longueur < MIN_LENGTH:
        print("\nAbuse pas mec, au moins 12 caractères, sinon tu vas te faire hacker\n")
        longueur = int(input("Aller retente une longueur convenable : "))

    # La longueur du mot de passe ne peut pas être supérieure à 50 caractères
    while longueur > MAX_LENGTH:
        print("\nBon t'es pas à la NASA, reste tranquille\n")
        longueur = int(input("Aller retente une longueur convenable : "))

    # On crée des variables qui contiennent chaque type de caractères
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # On s'assure d'avoir au moins un de chaque type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]

    # On vient ajouter la chaîne de caractères dans la liste vide "password"
    all_chars = lowercase + uppercase + digits + special
    # On s'assure bien de soustraire au total les 4 caractères spéciaux qu'on a déjà intégré précédemment
    for i in range(longueur-4):
        password.append(random.choice(all_chars))

    # Pour plus de sécurité, on mélange le mot de passe une fois constitué
    random.shuffle(password)

    print("\nOk ça me va, voici ton mot de passe :\n")

    # On concatène tous les caractères de la liste pour former le mot de passe final
    return ''.join(password)


# On demande à l'utilisateur combien de caractères il souhaite pour son mot de passe
while True:
    user_input = input(
        f"Combien de caractères tu veux pour ton mot de passe ? (Appuyez sur Entrée pour la valeur par défaut de {MIN_LENGTH}) ")

    if user_input == "":
        random_password = generate()  # Utilise la valeur par défaut
        break
    else:
        try:
            length = int(user_input)
            random_password = generate(length)
            break
        except ValueError:
            print("Oups ! Ce n'est pas un nombre valide. Essaie encore.")

print(random_password)
print(f"(longueur : {len(random_password)} caractères)")