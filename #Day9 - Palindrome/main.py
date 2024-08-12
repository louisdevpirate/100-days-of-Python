def palindrome_test(word):
    clean_word = word.lower().replace(" ", "")

    left_letter = 0
    right_letter = len(clean_word) - 1

    while left_letter <= right_letter:
        if clean_word[left_letter] != clean_word[right_letter]:
            return False
        left_letter += 1
        right_letter -= 1

    return True


test_word = input("Veuillez entrer le mot que vous souhaitez tester : ")
result = palindrome_test(test_word)

if result:
    print("Yo bien joué mec c'est un putain de palindrome ! Trop cooooool !")
else:
    print("Non désolé, ceci n'est pas un palindrome")