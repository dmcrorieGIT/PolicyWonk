import agent

class SimulatorGame:
    name = ""
    def __init__(self, name):
        self.name = name

    def test(self):
        jerry = agent.Agent(35, "white", "CIS", "Non-LGBTQ+", "middle")
        print("Hi my name is Jerry, I'm " + str(jerry.age) + " years old and my race is " + jerry.race)