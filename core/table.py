class Table:
    def __init__(self):
        self.players = []  # List to hold players at the table
        self.pot = 0  # Total amount in the pot
        self.community_cards = []  # Cards on the table
        self.current_bet = 0  # Current bet amount
        self.dealer_position = 0  # Position of the dealer

    