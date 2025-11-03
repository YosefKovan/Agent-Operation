from classes.Agent import Agent

class FieldAgent(Agent):

    def __init__(self, code_name, clearance_level, region):
        super().__init__(code_name, clearance_level)
        self.region = region

    def report(self):
        print(f"Code name : [{self.code_name}], Agent : [{self.clearance_level}], Region : [{self.region}]")


