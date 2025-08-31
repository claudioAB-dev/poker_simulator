from core.card import  card
from core.deck import deck


card = card()
mazo = card.generate_deck()


print(mazo)
deck = deck()
deck.shuffle()
print(deck.cards)
