import life_states

class LifeElements:
    health = 0
    income = 0
    education = 0
    pleasure = 0
    love = 0
    employment = 0
    law = 0
    social_attitudes = 0

    def __init__(self):
        self.health = life_states.Health(1, 1)
        self.income = life_states.Income(1, 1)
        self.education = life_states.Education(1, 1)
        self.pleasure = life_states.Pleasure(1, 1)
        self.love = life_states.Love(1, 1)
        self.employment = life_states.Employment(1, 1)
        self.law = life_states.Law(1, 1)
        self.social_attitudes = life_states.SocialAttitudes(1, 1)
