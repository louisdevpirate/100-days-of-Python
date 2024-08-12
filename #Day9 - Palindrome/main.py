import string
import unicodedata


def remove_accents(input_str):
    """
    Supprime les accents d'une chaîne de caractères.
    """
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])


def clean_text(text):
    """
    Nettoie le texte en supprimant la ponctuation, les espaces et les accents.
    """
    # Supprime la ponctuation et les espaces
    text = text.translate(str.maketrans("", "", string.punctuation)).replace(" ", "")
    # Convertit en minuscules et supprime les accents
    return remove_accents(text.lower())


def palindrome_test(word):
    """
    Vérifie si le mot ou la phrase est un palindrome.
    """
    clean_word = clean_text(word)

    left_letter = 0
    right_letter = len(clean_word) - 1

    while left_letter <= right_letter:
        if clean_word[left_letter] != clean_word[right_letter]:
            return False
        left_letter += 1
        right_letter -= 1

    return True


# Boucle principale pour permettre plusieurs tests
while True:
    test_word = input("Veuillez entrer le mot ou la phrase que vous souhaitez tester (ou 'q' pour quitter) : ")

    # Condition de sortie
    if test_word.lower() == 'q':
        print("Merci d'avoir utilisé le testeur de palindromes. À bientôt !")
        break

    result = palindrome_test(test_word)

    if result:
        print("Yo bien joué mec c'est un putain de palindrome ! Trop cOOool !")
    else:
        print("Non désolé, ceci n'est pas un palindrome. Bon, en même temps ça se voit non ?")

    print()  # Ligne vide pour la lisibilité