import life_states

class LifeElements:
    health = 0
    wealth = 0
    education = 0
    pleasure = 0
    love = 0
    employment = 0
    law = 0
    social_attitudes = 0

    def __init__(self):
        self.health = life_states.Health(1, 1)
        self.wealth = life_states.Wealth(2000)
        self.education = life_states.Education(1)
        self.pleasure = life_states.Pleasure(1)
        self.social_life = life_states.SocialLife(0.5)
        self.employment = life_states.Employment(200)
        self.law = life_states.Law(1, 1)
        self.social_attitudes = life_states.SocialAttitudes(1, 1)
