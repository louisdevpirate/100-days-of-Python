import random


class Deck:
    """
    Représente un jeu de cartes.
    """

    def __init__(self):
        """
        Initialise un nouveau jeu de cartes mélangé.
        """
        # Définit les couleurs et les valeurs des cartes
        suits = ['♠', '♥', '♦', '♣']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

        # Crée toutes les combinaisons possibles de valeurs et couleurs
        self.cards = [f"{value}{suit}" for suit in suits for value in values]

        # Mélange le jeu de cartes
        random.shuffle(self.cards)

    def draw(self):
        """
        Tire une carte du dessus du paquet.

        Returns:
            str or None: La carte tirée, ou None si le paquet est vide.
        """
        # Vérifie s'il reste des cartes, puis retire et renvoie la dernière carte
        return self.cards.pop() if self.cards else None


class Participant:
    """
    Classe de base pour les participants au jeu (joueur et croupier).
    """

    def __init__(self):
        """
        Initialise un participant avec une main vide.
        """
        self.cards = []

    def draw_card(self, deck):
        """
        Pioche une carte du paquet et l'ajoute à la main du participant.

        Args:
            deck (Deck): Le jeu de cartes à partir duquel piocher.

        Returns:
            str or None: La carte piochée, ou None si le paquet est vide.
        """
        card = deck.draw()
        if card:
            self.cards.append(card)
        return card

    def calculate_score(self):
        """
        Calcule le score de la main actuelle.

        Returns:
            int: Le score total de la main.
        """
        score = 0
        aces = 0
        for card in self.cards:
            value = card[:-1]  # Ignore le symbole de la couleur
            if value in ['J', 'Q', 'K']:
                score += 10
            elif value == 'A':
                aces += 1
            else:
                score += int(value)

        # Gère les as (1 ou 11 points)
        for _ in range(aces):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1

        return score

    def show_hand(self):
        """
        Affiche la main actuelle du participant.

        Returns:
            str: Une chaîne représentant toutes les cartes dans la main.
        """
        return ' '.join(self.cards)


class Player(Participant):
    """
    Représente le joueur dans le jeu de blackjack.
    """

    def make_decision(self):
        """
        Demande au joueur s'il veut piocher une autre carte.

        Returns:
            bool: True si le joueur veut piocher, False sinon.
        """
        decision = input("Voulez-vous piocher une carte ? (o/n) ").lower()
        return decision == 'o'


class Dealer(Participant):
    """
    Représente le croupier dans le jeu de blackjack.
    """

    def show_partial_hand(self):
        """
        Montre la première carte du croupier et cache la seconde.

        Returns:
            str: Une chaîne représentant la main partielle du croupier.
        """
        return f"{self.cards[0]} **"

    def should_draw(self):
        """
        Détermine si le croupier doit piocher une autre carte.

        Returns:
            bool: True si le score du croupier est inférieur à 17, False sinon.
        """
        return self.calculate_score() < 17


class Game:
    """
    Gère le déroulement d'une partie de blackjack.
    """

    def __init__(self):
        """
        Initialise une nouvelle partie avec un jeu de cartes, un joueur et un croupier.
        """
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def play(self):
        """
        Exécute une partie complète de blackjack.
        """
        # Distribution initiale
        for _ in range(2):
            self.player.draw_card(self.deck)
            self.dealer.draw_card(self.deck)

        # Tour du joueur
        while self.player.calculate_score() < 21:
            print(f"\nVotre main: {self.player.show_hand()} (Score: {self.player.calculate_score()})")
            print(f"Main du croupier: {self.dealer.show_partial_hand()}")

            if not self.player.make_decision():
                break

            self.player.draw_card(self.deck)

        # Tour du croupier
        while self.dealer.should_draw():
            self.dealer.draw_card(self.deck)

        # Affichage du résultat
        self.show_result()

    def show_result(self):
        """
        Affiche le résultat final de la partie.
        """
        player_score = self.player.calculate_score()
        dealer_score = self.dealer.calculate_score()

        print(f"\nVotre main finale: {self.player.show_hand()} (Score: {player_score})")
        print(f"Main finale du croupier: {self.dealer.show_hand()} (Score: {dealer_score})")

        if player_score > 21:
            print("Vous avez dépassé 21. Vous perdez.")
        elif dealer_score > 21:
            print("Le croupier a dépassé 21. Vous gagnez !")
        elif player_score > dealer_score:
            print("Vous gagnez !")
        elif player_score < dealer_score:
            print("Le croupier gagne.")
        else:
            print("Égalité.")


# Point d'entrée du programme
if __name__ == "__main__":
    game = Game()
    game.play()