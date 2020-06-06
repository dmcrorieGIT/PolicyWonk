import agent
import life_elements

class SimulatorGame:
    name = ""
    user_type = "human"
    game_in_progress = True

    def __init__(self, name, user_type):
        self.name = name
        self.user_type
        self.agent = 0
        self.life_elements = 0

    def start_simulation(self):
        self.build_simulation()
        while self.game_in_progress:
            if self.is_human():
                print("What action will you take?")
                action = int(input())
                self.invoke_action_on_number(action)

    def build_simulation(self):
        self.build_agent()
        self.build_life_elements()
    
    def build_agent(self):
        self.agent = agent.Agent("Andrew", 24, "Hispanic", "Non-Binary", "Male", "Lower Middle")

    def build_life_elements(self):
        self.life_elements = life_elements.LifeElements()

    def is_human(self):
        return self.user_type == "human"

    def invoke_action_on_number(self, number):
        if number == 0:
            self.study_action()
        elif number == 1:
            self.work_action()
        elif number == 2:
            self.anti_social_action()
        elif number == 3:
            self.socialize_action()
        elif number == 4:
            self.basic_pleasure_action()
        elif number == 99:
            self.game_in_progress = False

    #------------------------------------------------ Actions ---------------------------------------------------#
    def study_action(self):
        print("Agent studying")

    def work_action(self):
        print("Agent working")

    def anti_social_action(self):
        print("Agent stealing some shit")
    
    def socialize_action(self):
        print("Agent socializing")

    def basic_pleasure_action(self):
        print("Agent living that good life")
    #------------------------------------------------ Actions ---------------------------------------------------#

    def test(self):
        jerry = agent.Agent("Kyle", 35, "white", "CIS", "Non-LGBTQ+", "working")
        print("Hi my name is " + jerry.name + ", I'm " + str(jerry.age.years_old) + " years old")