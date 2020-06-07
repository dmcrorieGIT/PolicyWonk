import enum

class Attribute:
    pass

class Age(Attribute):
    years_old = 0
    def __init__(self, years_old):
        if years_old < 0 or years_old > 120:
            raise Exception("Age is not valid")

        self.years_old = years_old

class Race(Attribute):
    race_name = "White"
    permitted_values = ["White", "Hispanic", "Black", "Asian", "Native American", "Native Hawaiian", "Two or More", "Other"]
    def __init__(self, race_name):
        if race_name not in self.permitted_values:
            raise Exception("Race name not in permitted values")

        self.race_name = race_name

class Sex(Attribute):
    sex_classification = "Male"
    permitted_values = ["Male", "Female"]
    def __init__(self, sex_classification):
        if sex_classification not in self.permitted_values:
            raise Exception("Sex classification not in permitted values")

        self.sex_classification = sex_classification

class SexualOrientation(Attribute):
    sexual_orientation_name = "LGBTQ+"
    permitted_values = ["LGBTQ+", "Non-LGBTQ+"]
    def __init__(self, sexual_orientation_name):
        self.sexual_orientation_name = sexual_orientation_name

class SocialClass(Attribute):
    class_identification = "Underclass"
    permitted_values = ["Underclass", "Working Poor", "Working", "Lower Middle", "Upper Middle", "Lower Upper", "Upper Upper"]
    def __init__(self, class_identification):
        self.class_identification = class_identification
    
    def change_social_class(self, new_social_class):
        if new_social_class not in self.permitted_values:
            raise Exception("New social class not in permitted values")
        self.class_identification = new_social_class