# Création de la classe parent Personne
class Personne:

    def __init__(self, nom, age):
        self.nom = nom
        self.age = age


# Création de la classe enfant Etudiant qui hérite des attributs de parent
class Etudiant(Personne):
    def __init__(self, nom, age, niveau_etude):
        super().__init__(nom, age)
        # On vient créer un nouvel attribut niveau_etude pour la classe enfant
        self.niveau_etude = niveau_etude

