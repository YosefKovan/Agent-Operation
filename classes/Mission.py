

class Mission:

    def __init__(self, mission_game, target_location, assigned_agent):
        self.mission_game = mission_game
        self.target_location = target_location
        self.assigned_agent = assigned_agent

    def brief(self):
        print(f"Mission : [{self.mission_game}], Target : [{self.target_location}], Agent : [{self.assigned_agent}]")

        