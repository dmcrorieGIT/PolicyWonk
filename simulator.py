import agent
import life_elements
from os import system, name
import random

class SimulatorGame:
    name = ""
    user_type = "human"
    game_in_progress = True

    # constants
    TOTAL_NUMBER_OF_WEEKS = 80
    ACTIONS_ALLOWED_PER_WEEK = 3

    # game state information
    agent_in_play = 0
    life_element_state = 0
    number_of_weeks_passed = 0
    actions_performed_this_week = 0

    # education state information
    EDUCATION_PROGRAM_DROPOUT_CUTOFF = 60
    HIGHSCHOOL_DROPOUT_CUTOFF = 80
    WEEKS_NEEDED_FOR_HIGHSCHOOL_DIPLOMA = 156
    #WEEKS_NEEDED_FOR_ASSOCIATES_DEGREE = 104
    WEEKS_NEEDED_FOR_BACHELOR_DEGREE = 208
    WEEKS_NEEDED_FOR_MASTERS_DEGREE = 156
    WEEKS_NEEDED_FOR_PHD = 208
    in_study_program = False
    has_studied_this_week = False
    total_weeks_studied_in_program = 0
    study_weeks_missed = 0

    # employment state information
    WORK_WEEKS_MISSED_CAUSING_TERMINATION = 4
    WEEKS_NEEDED_SECOND_LEVEL = 70
    WEEKS_NEEDED_THIRD_LEVEL = 280
    WEEKS_NEEDED_FOURTH_LEVEL = 560
    work_weeks_missed = 0
    consecutive_weeks_worked = 0
    has_worked_this_week = False
    employment_static_amount = 200

    # socialization state information
    has_socialized_this_week = False

    # health state information
    has_practiced_self_care_this_week = False

    # anti-social behaviour informaiton
    NUMBER_OF_CRIMES_COMMITTED = 0

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
                        self.week_end()
                else:
                    self.end_game()

    def build_simulation(self):
        self.build_agent()
        self.build_life_elements()
    
    def build_agent(self):
        self.agent_in_play = agent.Agent("Andrew", 24, "Hispanic", "Non-Binary", "Male", "Underclass")

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

    def week_end(self):
        # TODO: check to see if the agent studied this week; if they didn't, add to number of weeks not studied. If the number
        # exceeds the threshold for the degree they are working towards (i.e., WEEKS_NEEDED_FOR_BACHELOR_DEGREE), then they drop out,
        # setting their in_study_program to False and their number_of_weeks_study to 0
        self.check_study()
        self.check_work()
        self.check_socialization()
        self.check_health()
        self.actions_performed_this_week = 0
        self.number_of_weeks_passed += 1
        self.new_week_start()

    def check_work(self):
        if self.has_worked_this_week:
            self.consecutive_weeks_worked += 1
        else:
            self.work_weeks_missed += 1

        # Terminated or Quit
        if self.work_weeks_missed >= self.WORK_WEEKS_MISSED_CAUSING_TERMINATION:
            self.life_element_state.employment.amount_per_week = 0
            self.consecutive_weeks_worked = 0

        if self.life_element_state.employment.amount_per_week == 0:
            return
        weeks_needed_for_promotion = self.get_weeks_needed_for_promotion(self.life_element_state.employment.amount_per_week)
        if self.consecutive_weeks_worked >= weeks_needed_for_promotion:
            self.promotion()
    
    def check_socialization(self):
        if not self.has_socialized_this_week:
            if not self.life_element_state.social_life.SocialWithdrawl(0.15):
                self.social_deprivation()
    
    def check_health(self):
        if not self.has_practiced_self_care_this_week:
            if not self.life_element_state.health.decrease_in_mental_health(0.1):
                self.mental_health_problems()
            if not self.life_element_state.health.decrease_in_physical_health(0.1):
                self.physical_health_problems()

    def promotion(self):
        amount_per_week = self.life_element_state.employment.amount_per_week
        
        if amount_per_week == 200:
            self.life_element_state.employment.raise_employment_status(500)
            self.employment_static_amount = 500
        elif amount_per_week == 500:
            self.life_element_state.employment.raise_employment_status(1000)
            self.employment_static_amount = 1000
        elif amount_per_week == 1000:
            self.life_element_state.employment.raise_employment_status(2000)
            self.employment_static_amount = 2000

    def check_study(self):
        if self.in_study_program:
            if not self.has_studied_this_week:
                self.study_weeks_missed + 1
                if self.study_weeks_missed >= self.EDUCATION_PROGRAM_DROPOUT_CUTOFF:
                    dropout_check = self.random_roll()
                    if dropout_check <= 0.2:
                        self.in_study_program = False
                        print("You've Dropped Out.")
                    else:
                        print("Dean's Warning: Miss more school and you will be expelled.")
        


    def new_week_start(self):
        weekly_upkeep = self.weekly_upkeep_per_social_class(self.agent_in_play.social_class.class_identification, self.life_element_state.wealth.money)
        if not self.life_element_state.wealth.Withdraw(weekly_upkeep):
            self.debt_consequences()
        print("Starting a new week, upkeep: " + str(weekly_upkeep) + " \n")
        self.has_worked_this_week = False
        self.has_socialized_this_week = False
        self.has_practiced_self_care_this_week = False

    #------------------------------------------------ Actions ---------------------------------------------------#

    def study_action(self):
        # TODO: check to see if is_in_study_program; if they aren't, the study action does a random roll to see if they
        # enroll. If they are already in a study program, then:
        #         1. add to number of weeks studied in program
        #         2. set the value of studied_this_week to True
        
        
        if not self.in_study_program:
            enrollment_check = self.random_roll()
            if enrollment_check >= 0.2: #have check affected by attributes
                self.in_study_program = True
                
        else:
            self.has_studied_this_week = True
            self.total_weeks_studied_in_program += 1
            
            education_level = self.life_element_state.education.level
            
            if education_level == 1:
                if self.total_weeks_studied_in_program >= self.WEEKS_NEEDED_FOR_HIGHSCHOOL_DIPLOMA:
                    self.life_element_state.education.education_level_up()
                    self.in_study_program = False
                    print("Congratulations! You've graduated with a Highschool Diploma.")
            elif education_level == 2:
                if self.total_weeks_studied_in_program >= self.WEEKS_NEEDED_FOR_BACHELOR_DEGREE:
                    self.life_element_state.education.education_level_up()
                    self.in_study_program = False
                    print("Congratulations! You've graduated with a Bachelor's Degree.")
            elif education_level == 3:
                if self.total_weeks_studied_in_program >= self.WEEKS_NEEDED_FOR_MASTERS_DEGREE:
                    self.life_element_state.education.education_level_up()
                    self.in_study_program = False
                    print("Congratulations! You've graduated with a Master's Degree.")
            elif education_level == 4:
                if self.total_weeks_studied_in_program >= self.WEEKS_NEEDED_FOR_PHD:
                    self.life_element_state.education.education_level_up()
                    self.in_study_program = False
                    print("Congratulations! You've graduated with a PhD.")
            else:
                print("Agent studying")
            
        

    def work_action(self):
        if self.life_element_state.employment.amount_per_week > 0:
            self.has_worked_this_week = True
            self.consecutive_weeks_worked += 1
            amount_earned = self.life_element_state.education.level * self.life_element_state.employment.amount_per_week
            self.life_element_state.wealth.Deposit(amount_earned)
            print("Agent working, made " + str(amount_earned) + "$")
        else:
            self.work_weeks_missed = 0
            self.has_worked_this_week = True
            print("Agent looking for work")
            if (self.look_for_work()):
                self.life_element_state.employment.raise_employment_status(self.employment_static_amount)
                print("Agent found work!")
            else:
                print("Agent did not find work...")

    def anti_social_action(self):
        #agent commits crime - recieves wealth, becomes better, chance of police
        if self.NUMBER_OF_CRIMES_COMMITTED != 0:
            crime_multiplier = 1 + self.NUMBER_OF_CRIMES_COMMITTED/10
        
        amount_earned = (self.life_element_state.education.level * (2*self.life_element_state.employment.amount_per_week)) * crime_multiplier
        print("Agent is committing a crime. Will they be caught?")

        investigation = self.random_roll() + self.NUMBER_OF_CRIMES_COMMITTED/100
        if investigation >= 0.95:
            print("Agent is caught. Incarceration")
            #incarceration action
        else:
            print("Crime is a success! You've gotten better at it.")
            print("Agent Earned $" + amount_earned)
            self.life_element_state.wealth.Deposit(amount_earned)

    
    def socialize_action(self):
        self.life_element_state.social_life.Socialize(0.1)
        self.has_socialized_this_week = True
        print("Agent socializing")

    def basic_pleasure_action(self):
        print("Agent living that good life")
    
    def self_care_action(self):
        self.life_element_state.health.self_care(0.15, 0.15)
        self.has_practiced_self_care_this_week = True
        print("Agent is taking care of himself")

    def print_stats(self):
        print("Total weeks passed: " + str(self.number_of_weeks_passed))
        print("Actions taken this week: " + str(self.actions_performed_this_week))
        print("")
        print("Social Attitudes: " + self.percentage_from_float(self.life_element_state.social_attitudes.average_value()))
        print("Health: " + self.percentage_from_float(self.life_element_state.health.average_value()))
        print("Wealth: " + str(self.life_element_state.wealth.money))
        print("Education: " + self.educational_attainment_from_tier(self.life_element_state.education.level))
        print("Pleasure: " + self.percentage_from_float(self.life_element_state.pleasure.average_value()))
        print("Social Life: " + self.percentage_from_float(self.life_element_state.social_life.satisfaction))
        print("Employment: " + str(200) + "$ /week")
        print("Law: " + self.percentage_from_float(0.3))
        print("")

    #------------------------------------------------ Actions ---------------------------------------------------#

    #---------------------------------------------- Sub-Actions -------------------------------------------------#

    def look_for_work(self):
        # TODO: make this based on agent attribute data
        # TODO: make this be affected by policy
        return self.random_roll() > 0.2

    #---------------------------------------------- Sub-Actions -------------------------------------------------#
    #---------------------------------------------Attribute Checks-----------------------------------------------#
    def agent_attribute_checks(self):
        return self.agent_in_play.get_agent_attribute()

    def education_attribute_modifiers(self):
        pass
        

    
    
    #---------------------------------------------Attribute Checks-----------------------------------------------#

    #--------------------------------------------- Consequences --------------------------------------------------#

    def social_deprivation(self):
        # TODO: social deprivation, cause problems with the other states if this is reached
        print("Experiencing negative effects of social deprivation...")

    def debt_consequences(self):
        # TODO: If we're here, that means the agent just went into debt, we need to make bad things happen here
        print("Uh-oh, looks like somebody's in debt ;)")

    def mental_health_problems(self):
        # TODO: cause problems elsewhere when this is reached
        print("Experiencing mental health issues")
    
    def physical_health_problems(self):
        # TODO: cause problems elsewhere when this is reached
        print("Experiencing physical health issues")

    #--------------------------------------------- Consequences --------------------------------------------------#

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
            return "Bachelors degree"
        elif 4:
            return "Masters degree"
        elif 5:
            return "Doctorate (PhD)"

    def random_roll(self):
        return random.randint(0,1)
    
    def weekly_upkeep_per_social_class(self, social_class, total_wealth):
        # ["Underclass", "Working Poor", "Working", "Lower Middle", "Upper Middle", "Lower Upper", "Upper Upper"]
        if total_wealth < 9000:
            total_wealth = 9000
        total_wealth_by_weeks = total_wealth / 52
        if social_class == "Underclass":
            percent_of_total_wealth = 0.95
        elif social_class == "Working Poor":
            percent_of_total_wealth = 0.92
        elif social_class == "Working":
            percent_of_total_wealth = 0.82
        elif social_class == "Lower Middle":
            percent_of_total_wealth = 0.76
        elif social_class == "Upper Middle":
            percent_of_total_wealth = 0.65
        elif social_class == "Lower Upper":
            percent_of_total_wealth = 0.40
        elif social_class == "Upper Upper":
            percent_of_total_wealth = 0.12

        return int(total_wealth_by_weeks * percent_of_total_wealth)

    def get_weeks_needed_for_promotion(self, amount_per_week):
        if amount_per_week == 200:
            return self.WEEKS_NEEDED_SECOND_LEVEL
        elif amount_per_week == 500:
            return self.WEEKS_NEEDED_THIRD_LEVEL
        elif amount_per_week == 1000:
            return self.WEEKS_NEEDED_FOURTH_LEVEL

    #------------------------------------------------- Utils -----------------------------------------------------#