import random

class AIPlayer:
    ALLOWED_GAME_ACTIONS = [0, 1, 2, 3, 4, 5, 90, 91, 98, 99]

    def __init__(self):
        pass

    def make_decision(self):
        return self.ALLOWED_GAME_ACTIONS[self.calculate_decision()]
    
    def calculate_decision(self):
        return random.randint(0,5)
