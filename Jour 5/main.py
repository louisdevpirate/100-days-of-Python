import re


def main():
    try:
        with open('fichier.txt', 'r') as fichier:
            content = fichier.read()
        return content
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
    except IOError:
        print("Une erreur s'est produite lors de la lecture du fichier.")

