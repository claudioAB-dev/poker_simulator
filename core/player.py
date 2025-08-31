class Player:
    def __init__(self):
        self.name = ""
        self.state = ""
        self.stack = 0
        self.hand = []  # List to hold the player's cards
        self.is_turn = False