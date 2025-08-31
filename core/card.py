class card:
    def generate_deck(self):
        suit = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        return [(r, s) for r in rank for s in suit]