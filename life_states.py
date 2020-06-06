class LifeState:
    pass

class Health(LifeState):
    mental_health = 0.5
    physical_health = 0.5

    def __init__(self, mental_health, physical_health):
        self.mental_health = mental_health
        self.physical_health = physical_health

class Income(LifeState):
    category_1 = 0.5
    category_2 = 0.5

    def __init__(self, category_1, category_2):
        self.category_1 = category_1
        self.category_2 = category_2

class Education(LifeState):
    category_1 = 0.5
    category_2 = 0.5

    def __init__(self, category_1, category_2):
        self.category_1 = category_1
        self.category_2 = category_2

class Pleasure(LifeState):
    category_1 = 0.5
    category_2 = 0.5

    def __init__(self, category_1, category_2):
        self.category_1 = category_1
        self.category_2 = category_2

class Love(LifeState):
    category_1 = 0.5
    category_2 = 0.5

    def __init__(self, category_1, category_2):
        self.category_1 = category_1
        self.category_2 = category_2

class Employment(LifeState):
    category_1 = 0.5
    category_2 = 0.5

    def __init__(self, category_1, category_2):
        self.category_1 = category_1
        self.category_2 = category_2

class Law(LifeState):
    category_1 = 0.5
    category_2 = 0.5

    def __init__(self, category_1, category_2):
        self.category_1 = category_1
        self.category_2 = category_2

class SocialAttitudes(LifeState):
    category_1 = 0.5
    category_2 = 0.5

    def __init__(self, category_1, category_2):
        self.category_1 = category_1
        self.category_2 = category_2