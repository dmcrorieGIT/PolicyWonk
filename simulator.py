import agent
import life_elements
from os import system, name

class SimulatorGame:
    name = ""
    user_type = "human"
    game_in_progress = True

    # constants
    TOTAL_NUMBER_OF_WEEKS = 8
    ACTIONS_ALLOWED_PER_WEEK = 3
    EDUCATION_PROGRAM_DROPOUT_CUTOFF = 60
    WORK_WEEKS_MISSED_CAUSING_TERMINATION = 4

    # game state information
    agent_in_play = 0
    life_element_state = 0
    number_of_weeks_passed = 0
    actions_performed_this_week = 0

    # education state information
    in_study_program = False
    study_weeks_missed = 0

    # employment state information
    work_weeks_missed = 0


    def __init__(self, name, user_type):
        self.name = name
        self.user_type
        self.agent = 0
        self.life_elements = 0

    def start_simulation(self):
        self.build_simulation()
        while self.game_in_progress:
            if self.is_human():
                if self.has_not_exceeded_game_time():
                    if self.has_not_exceeded_weekly_actions():
                        print("Select an action to perform: \n[0]Study \n[1]Work \n[2]Anti-Social Action \n[3]Socialize \n[4]Basic Pleasure \n[5]Self Care \n[90]See stats")
                        action_to_perform = int(input())
                        system('clear')
                        if self.invoke_action_on_number(action_to_perform):
                            self.actions_performed_this_week += 1
                    else:
                        self.actions_performed_this_week = 0
                        self.number_of_weeks_passed += 1
                        self.new_week_start()
                else:
                    self.end_game()

    def build_simulation(self):
        self.build_agent()
        self.build_life_elements()
    
    def build_agent(self):
        self.agent_in_play = agent.Agent("Andrew", 24, "Hispanic", "Non-Binary", "Male", "Lower Middle")

    def build_life_elements(self):
        self.life_element_state = life_elements.LifeElements()

    # -------------------------------- Checks ---------------------------------------------#
    def is_human(self):
        return self.user_type == "human"

    def has_not_exceeded_game_time(self):
        return self.number_of_weeks_passed <= self.TOTAL_NUMBER_OF_WEEKS

    def has_not_exceeded_weekly_actions(self):
        return self.actions_performed_this_week < self.ACTIONS_ALLOWED_PER_WEEK
    # -------------------------------- Checks ---------------------------------------------#

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
        elif number == 5:
            self.self_care_action()
        elif number == 90:
            self.print_stats()
            return False
        elif number == 99:
            self.game_in_progress = False
        else:
            print("Invalid action, please pay the fuck attention next time")
            return False
        print("\n")
        return True

    def new_week_start(self):
        print("Starting a new week... \n")

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
    
    def self_care_action(self):
        print("Agent is taking care of himself")

    def print_stats(self):
        print("Total weeks passed: " + str(self.number_of_weeks_passed))
        print("Actions taken this week: " + str(self.actions_performed_this_week))
        print("")
        print("Social Attitudes: " + self.percentage_from_float(0.4))
        print("Health: " + self.percentage_from_float(0.5))
        print("Wealth: " + str(3400))
        print("Education: " + self.educational_attainment_from_tier(2))
        print("Pleasure: " + self.percentage_from_float(0.72))
        print("Social Life: " + self.percentage_from_float(0.84))
        print("Employment: " + str(200) + "$ /week")
        print("Law: " + self.percentage_from_float(0.3))
        print("")
    #------------------------------------------------ Actions ---------------------------------------------------#


    #------------------------------------------------- Utils -----------------------------------------------------#
    def test(self):
        print("Testing...")

    def end_game(self):
        print("Simulation has ended, thanks for playing!")
        self.game_in_progress = False
    
    def percentage_from_float(self, value):
        return str(value * 100)
    
    def educational_attainment_from_tier(self, tier):
        if 1:
            return "Less than highschool"
        elif 2:
            return "Highschool diploma and/or some college"
        elif 3:
            return "Associates degree or trade certificate"
        elif 4:
            return "Bachelors degree"
        elif 5:
            return "Masters degree"
        elif 6:
            return "Doctorate (PhD)"
    #------------------------------------------------- Utils -----------------------------------------------------#