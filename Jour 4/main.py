import random
import string


def generate(longueur):
    while longueur < 12:
        print("\nAbuse pas mec, au moins 12 caractères, sinon tu vas te faire hacker\n")
        longueur = int(input("Aller retente une longueur convenable : "))

    while longueur > 50:
        print("\nBon t'es pas à la NASA, reste tranquille\n")
        longueur = int(input("Aller retente une longueur convenable : "))

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

    all_chars = lowercase + uppercase + digits + special
    for i in range(longueur-4):
        password.append(random.choice(all_chars))

    random.shuffle(password)

    print("\nOk ça me va, voici ton mot de passe :\n")
    return ''.join(password)


password_lenght = generate(int(input("Combien de caractères tu veux pour ton mot de passe ? ")))

print(password_lenght)