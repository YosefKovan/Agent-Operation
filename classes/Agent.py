
class Agent:

    total_agents = 0

    def __init__(self, code_name, clearance_level):
        self.code_name = code_name
        self.clearance_level = clearance_level
        Agent.total_agents += 1

    def report(self):
        print(f"Agent [{self.code_name}] reporting. clearance level [{self.clearance_level}]")

    def set_clearance_level(self, clearance_level):

        if 0 < clearance_level < 11:
            self._clearance_level = clearance_level
        else:
            print("Clearance level must be greater then 0 and smaller then 11")


    def get_clearance_level(self):
        return self._clearance_level

    @staticmethod
    def get_total_agents():
        print("total number of agents: ", Agent.total_agents)

