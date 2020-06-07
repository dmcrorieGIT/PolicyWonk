import agent_attributes

class Agent:
    name = "Bob"
    age = 0
    race = 0
    gender = 0
    sexual_orientation = 0
    sex = 0
    social_class = 0

    def __init__(self, name, years_old, race_name, sexual_orientation_name, sex_name, class_identification):
        self.name = name
        self.age = agent_attributes.Age(years_old)
        self.race = agent_attributes.Race(race_name)
        self.sexual_orientation = agent_attributes.SexualOrientation(sexual_orientation_name)
        self.sex = agent_attributes.Sex(sex_name)
        self.social_class = agent_attributes.SocialClass(class_identification)

    def test(self):
        print("Agent's age is: " + self.age.years_old)

    def get_agent_attribute(self):
        return [self.age, self.race, self.sexual_orientation, self.sex, self.social_class]

