# Dictionnaire pour encoder (lettre vers morse)
morse_encode = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'  # Espace pour séparer les mots
}

# Dictionnaire pour décoder (morse vers lettre)
morse_decode = {value: key for key, value in morse_encode.items()}


def encode_to_morse(sentence):
    morse_message = []
    for character in sentence:
        if character in morse_encode:
            morse_message.append(morse_encode[character])
        else:
            print(f"Le langage morse c'est pas du putain de chinois mandarin, remballe ton {character.lower()}")

    # Joindre tous les caractères morse avec un espace
    return " ".join(morse_message)


def decode_to_letters(morse):
    letters_message = []
    morse_characters = morse.split()  # Sépare la chaîne en caractères morse individuels
    for character in morse_characters:
        if character in morse_decode:
            letters_message.append(morse_decode[character])
        else:
            letters_message.append('?')  # Pour les caractères non reconnus

    return ''.join(letters_message)  # Joindre sans espace entre les lettres


while True:
    try:
        selection = input("Voulez vous encoder ou décoder un message ? (Encoder/Décoder/Quitter)\n").lower()

        if selection == 'quitter':
            print("Au revoir !")
            break

        elif selection == 'encoder':
            encode = input("Entrez votre message à traduire en morse : ").upper()
            result = encode_to_morse(encode)
            print("Message en morse :", result)

        elif selection == 'decoder' or selection == 'décoder':
            decode = input("Entrez votre message à traduire depuis le morse : ")
            result = decode_to_letters(decode)
            print("Message en lettres :", result)

        else:
            print("Option non reconnue. Veuillez choisir 'Encoder', 'Décoder' ou 'Quitter'.\n")
            continue

    except Exception as e:
        print(f"Une erreur s'est produite : {e}")
        print("Essayons à nouveau.")

    print("\n")  # Ligne vide pour plus de clarté entre les itérations





