class StatusQuo:

    def __init__(self):
        pass

    raceDict = {
        "White":{
            "Illness": 0.0075,
            "Depression":.0204,
            "Education": 0.0039,
            "Law": 0.00450
        },
        "Hispanic":{
            "Illness": 0.0190,
            "Depression": .0152,
            "Education": 0.0065,
            "Law": 0.00831
        },
        "Black":{
            "Illness": 0.0115,
            "Depression": .0162,
            "Education": 0.0055,
            "Law": 0.02306
        },
        "Asian":{
            "Illness": 0.0068,
            "Depression": .0145,
            "Education": 0.0047,
            "Law": 0.00115
            },
        "Native American":{
            "Illness": 0.0218,
            "Depression": .0189,
            "Education": 0.0044,
            "Law": 0.01291
            },
        "Native Hawaiian":{
            "Illness": 0.0093,
            "Depression": .0194,
            "Education": 0.0044,
            "Law": 0.01017
            },
        "Two or More":{
            "Illness": 0.0080,
            "Depression": .0286,
            "Education": 0.0050,
            "Law": 0.00831
            }
        # ,"Other":{
        #     "Illness": #,
        #     "Depression":#,
        #     "Education":#,
        #     "Law":#
        #     }
    }

    sexDict = {
        "Male":{
            "Illness": 0.00459,
            "Depression": .0151,
            "Education": 0.0070,
            "Law": 0.0054
            },
        "Female":{
            "Illness": 0.00391,
            "Depression":.0223,
            "Education": 0.0050,
            "Law": 0.0046
            }
    }

    sexualOrientDict = {
        "LGBTQ+": {
            "Illness":0.0050,
            "Depression": 0.039,
            "Education": 0.0062,
            "Law": 0.0025
        },
        "Non-LGBTQ+":{
            "Illness":0.0025,
            "Depression": 0.0167,
            "Education": 0.0022,
            "Law": 0.0023
        }
    }

    socialClassDict = {
        "Underclass": {
            "Illness": 0.0378,
            "Depression": 0.0087,
            #"Education":#,
            "Law": 0.00518,
            #"Residual Wealth":#
            "Taxes": 0.10
            },
        "Working Poor": {
            "Illness": 0.0332,
            "Depression": 0.0087,
            #"Education":#,
            "Law":0.00572,
            #"Residual Wealth":#
            "Taxes": 0.12
            },
        "Working": {
            "Illness": 0.0166,
            "Depression": 0.0051,
            #"Education":#,
            "Law":0.00540,
            #"Residual Wealth":# 
            "Taxes": 0.17
        },
        "Lower Middle": {
            "Illness": 0.0080,
            "Depression": 0.0027,
            #"Education":#,
            "Law":0.00320,
            #"Residual Wealth":#,
            "Taxes": 0.23
        },
        "Upper Middle": {
            "Illness":0.0050,
            "Depression": 0.0027,
            #"Education":#,
            "Law": 0.0011,
            #"Residual Wealth":#,
            "Taxes": 0.27
        },
        "Lower Upper": {
            "Illness": 0,
            "Depression":0.0012,
            #"Education":#,
            "Law": -0.0030,
            #"Residual Wealth":#,
            "Taxes":0.37
        },
        "Upper Upper": {
            "Illness":0,
            "Depression": 0.0012,
            #"Education":#,
            "Law":-0.0050,
            #"Residual Wealth":#,
            "Taxes": 0.37
        }
    }

    def looking_for_work_percentage(self):
        # TODO: do dis
        return 0.2
    
    def taxes(self, agent_characteristics):
        # TODO: do dis
        return self.socialClassDict[agent_characteristics[4].class_identification]["Taxes"]

    def depression_percentage(self):
        # TODO: do this as well
        return 0.2

    def illness_percentage(self):
        # TODO: do this as well
        return 0.2

    def education_percentage(self, attributes):
        raceMod = raceDict[attributes[1]]["Education"]
        sexualOrientMod = sexualOrientDict[attributes[2]]["Education"]
        sexMod = sexDict[attributes[3]]["Education"]
        socialClassMod = socialClassDict[attributes[4]]["Education"] 

        new value = 0.95 - raceMod - sexualOrientMod - sexMod - socialClassMod
        return 0.2
    
    def law_percentage(self, attributes, roll):
        
        return 0.95

