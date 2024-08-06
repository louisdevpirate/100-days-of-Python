# Jour 5 : Créez un programme qui lit un fichier texte, compte le nombre d'occurrences de chaque mot et affiche les 5 mots les plus fréquents.

import re


def main():
    try:
        with open('planning.txt', 'r') as fichier:
            content = fichier.read()
        words = extract_words(content)
        words_counts = count_words(words)
        print_top_words(words_counts)
    except FileNotFoundError:
        print("Le fichier n'a pas été trouvé.")
    except IOError:
        print("Une erreur s'est produite lors de la lecture du fichier.")


def extract_words(content):
    return re.findall(r'\b\w+\b', content.lower())


def count_words(words):
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


def print_top_words(words_counts):
    sorted_words = sorted(words_counts.items(), key=lambda x: x[1], reverse=True)
    print("Les 5 mots les plus fréquents sont:")
    for word, count in sorted_words[:5]:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()



