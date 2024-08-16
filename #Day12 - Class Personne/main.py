class Personne:
    """Représente une personne avec un nom et un âge."""

    def __init__(self, nom, age):
        """
        Initialise une nouvelle personne.

        :param nom: Le nom de la personne
        :param age: L'âge de la personne
        """
        self.nom = nom
        self.set_age(age)

    def set_age(self, age):
        """Définit l'âge de la personne avec validation."""
        if age < 0:
            raise ValueError("L'âge ne peut pas être négatif")
        self._age = age

    def get_age(self):
        """Retourne l'âge de la personne."""
        return self._age

    def __str__(self):
        """Retourne une représentation en chaîne de la personne."""
        return f"Personne: {self.nom}, {self._age} ans"


class Etudiant(Personne):
    """Représente un étudiant, qui est une personne avec un niveau d'études."""

    def __init__(self, nom, age, niveau_etude):
        """
        Initialise un nouvel étudiant.

        :param nom: Le nom de l'étudiant
        :param age: L'âge de l'étudiant
        :param niveau_etude: Le niveau d'études de l'étudiant
        """
        super().__init__(nom, age)
        self.niveau_etude = niveau_etude

    def __str__(self):
        """Retourne une représentation en chaîne de l'étudiant."""
        return f"Etudiant: {self.nom}, {self.get_age()} ans, Niveau: {self.niveau_etude}"