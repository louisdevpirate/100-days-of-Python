# Dictionnaire pour encoder (lettre vers morse)
morse_encode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': ' '  # Espace pour séparer les mots
}

# Dictionnaire pour décoder (morse vers lettre)
# Inverse le dictionnaire morse_encode pour créer morse_decode
morse_decode = {value: key for key, value in morse_encode.items()}


def encode_to_morse(sentence):
    """
    Encode une phrase en code morse.

    Args:
        sentence (str): La phrase à encoder.

    Returns:
        str: La phrase encodée en morse.
    """
    morse_message = []
    for character in sentence:
        if character in morse_encode:
            morse_message.append(morse_encode[character])
        else:
            print(f"Le langage morse c'est pas du putain de chinois mandarin, remballe ton {character.lower()}")

    # Joindre tous les caractères morse avec un espace
    return " ".join(morse_message)


def decode_to_letters(morse):
    """
    Décode un message en code morse vers des lettres.

    Args:
        morse (str): Le message en code morse à décoder.

    Returns:
        str: Le message décodé en lettres.
    """
    words = morse.split('   ')  # 3 espaces entre les mots
    decoded_words = []
    for word in words:
        decoded_word = ''.join(morse_decode.get(char, '?') for char in word.split())
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)


# Boucle principale du programme
while True:
    try:
        # Demande à l'utilisateur de choisir une action
        selection = input("Voulez vous encoder ou décoder un message ? (Encoder/Décoder/Quitter)\n").lower()

        if selection == 'quitter':
            print("Au revoir !")
            break

        elif selection == 'encoder':
            # Encodage d'un message
            encode = input("Entrez votre message à traduire en morse : ").upper()
            result = encode_to_morse(encode)
            print("Message en morse :", result)

        elif selection == 'decoder' or selection == 'décoder':
            # Décodage d'un message
            decode = input("Entrez votre message à traduire depuis le morse : ")
            result = decode_to_letters(decode)
            print("Message en lettres :", result)

        else:
            # Gestion des entrées non valides
            print("Option non reconnue. Veuillez choisir 'Encoder', 'Décoder' ou 'Quitter'.\n")
            continue

    except Exception as e:
        # Gestion des erreurs générales
        print(f"Une erreur s'est produite : {e}")
        print("Essayons à nouveau.")

    print("\n")  # Ligne vide pour plus de clarté entre les itérations