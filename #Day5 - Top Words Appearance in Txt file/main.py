# #Day5 - Top Words Appearance in Txt file : Créez un programme qui lit un fichier texte, compte le nombre d'occurrences de chaque mot et affiche les 5 mots les plus fréquents.

import re


def main():
    try:
        # Ouvre et lit le contenu du fichier 'planning.txt'
        with open('fichier.txt', 'r') as fichier:
            content = fichier.read()
        # Extrait les mots du contenu
        words = extract_words(content)
        # Compte les occurrences de chaque mot
        words_counts = count_words(words)
        # Affiche les 5 mots les plus fréquents
        print_top_words(words_counts)
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
    except IOError:
        print("Une erreur s'est produite lors de la lecture du fichier.")


def extract_words(content):
    # Utilise une expression régulière pour trouver tous les mots
    # et les convertit en minuscules
    return re.findall(r'\b\w+\b', content.lower())


def count_words(words):
    word_counts = {}
    for word in words:
        # Si le mot est déjà dans le dictionnaire, incrémente son compteur
        # Sinon, ajoute le mot au dictionnaire avec un compteur initial de 1
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def print_top_words(words_counts):
    # Trie les mots par leur nombre d'occurrences, du plus fréquent au moins fréquent
    sorted_words = sorted(words_counts.items(), key=lambda x: x[1], reverse=True)
    print("Les 5 mots les plus fréquents sont:")
    # Affiche les 5 premiers mots de la liste triée
    for word, count in sorted_words[:5]:
        print(f"{word}: {count}")


# Vérifie si le script est exécuté directement (et non importé comme un module)
if __name__ == "__main__":
    main()