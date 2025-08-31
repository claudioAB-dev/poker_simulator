
class deck:
    """Class to represent a deck of cards."""
    from core.card import card
    card = card()
    deck1 = card.generate_deck()
    
    def __init__(self):
        self.cards = deck.deck1
    def shuffle(self):
        """Shuffle the deck of cards."""
        import random
        return(random.shuffle(self.cards))
