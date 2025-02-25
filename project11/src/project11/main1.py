from crewai.flow.flow import Flow,start
from project11.crews.dev_crew.dev_crew import DevCrew



class DevFlow(Flow):
    @start()
    def development(self):
        result = DevCrew().crew().kickoff(
            inputs={"problem":"Write a function for addition two numbers."}
        )
        return result.raw
    



def kickoff()->None:
    obj = DevFlow()
    final_output = obj.kickoff()
    print(final_output)
