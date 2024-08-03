# Day 1 : Créez un programme qui demande le nom de l'utilisateur et son âge, puis affiche dans combien d'années il aura 100 ans.

name = input("Quel est votre nom ? ") # Demande le nom
age = int(input("Quel est votre âge ? ")) # Demande l'age

print(f"Merci pour ces informations {name}. Pour atteindre les 100 ans, il vous reste encore {100-age} à vivre.") #Affiche le résulat