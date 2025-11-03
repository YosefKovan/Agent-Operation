from classes.Agent import Agent
from classes.FieldAgent import FieldAgent
from classes.CyberAgent import CyberAgent

def call_report_agent(agents):
    for agent in agents:
        agent.report()

def create_agents():
    lst = []
    aget1 = Agent("agent1", 1)
    lst.append(aget1)
    agent2 = FieldAgent("agent2", 2, "ls")
    lst.append(agent2)
    agent3 = CyberAgent("agent3", 4, "united states")
    lst.append(agent3)

    Agent.get_total_agents()

    return lst


if __name__ == "__main__":
    agents = create_agents()
    call_report_agent(agents)