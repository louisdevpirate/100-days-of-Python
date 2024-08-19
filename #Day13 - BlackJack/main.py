import random


class Deck:
    def __init__(self):
        suits = ['♠', '♥', '♦', '♣']
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.cards = [f"{value}{suit}" for suit in suits for value in values]
        random.shuffle(self.cards)


class Participant:
    def __init__(self):
        self.cards = []

    def draw_card(self, deck):
        card = deck.draw()
        if card:
            self.cards.append(card)
        return card

    def calculate_score(self):
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

        for _ in range(aces):
            if score + 11 <= 21:
                score += 11
            else:
                score += 1

        return score

    def show_hand(self):
        return ' '.join(self.cards)


class Player(Participant):
    def make_decision(self):
        decision = input("Voulez-vous piocher une carte ? (o/n) ").lower()
        return decision == 'o'


class Dealer(Participant):
    def show_partial_hand(self):
        return f"{self.cards[0]} **"

    def should_draw(self):
        return self.calculate_score() < 17


class Game:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()

    def play(self):
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

        # Résultat
        self.show_result()

    def show_result(self):
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


# Lancer le jeu
if __name__ == "__main__":
    game = Game()
    game.play()

