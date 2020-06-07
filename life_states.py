class LifeState:
    pass

class Health(LifeState):
    mental_health = 0.5
    physical_health = 0.5

    def __init__(self, mental_health, physical_health):
        self.mental_health = mental_health
        self.physical_health = physical_health

    def average_value(self):
        return (self.mental_health + self.physical_health) / 2

class Wealth(LifeState):
    money = 0

    def __init__(self, money):
        self.money = money

    def Withdraw(self, amount):
        self.money -= amount
        # if this withdraw put them in the negative, then return
        # 'False' for in debt
        return self.money > 0

    def Deposit(self, amount):
        self.money += amount

class Education(LifeState):
    level = 0

    def __init__(self, level):
        self.level = level

class Pleasure(LifeState):
    category_1 = 0.5
    category_2 = 0.5

    def __init__(self, category_1, category_2):
        self.category_1 = category_1
        self.category_2 = category_2

    def average_value(self):
        return (self.category_1 + self.category_2) / 2

class SocialLife(LifeState):
    category_1 = 0.5
    category_2 = 0.5

    def __init__(self, category_1, category_2):
        self.category_1 = category_1
        self.category_2 = category_2

    def average_value(self):
        return (self.category_1 + self.category_2) / 2

class Employment(LifeState):
    amount_per_week = 0

    def __init__(self, amount_per_week):
        self.amount_per_week = amount_per_week

    def average_value(self):
        return (self.category_1 + self.category_2) / 2
    
    def raise_employment_status(self, amount):
        self.amount_per_week = amount

class Law(LifeState):
    category_1 = 0.5
    category_2 = 0.5

    def __init__(self, category_1, category_2):
        self.category_1 = category_1
        self.category_2 = category_2

    def average_value(self):
        return (self.category_1 + self.category_2) / 2

class SocialAttitudes(LifeState):
    category_1 = 0.5
    category_2 = 0.5

    def __init__(self, category_1, category_2):
        self.category_1 = category_1
        self.category_2 = category_2
    
    def average_value(self):
        return (self.category_1 + self.category_2) / 2