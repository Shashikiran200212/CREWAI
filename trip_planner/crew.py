from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()


@CrewBase
class TripPlanner:
    """TripPlanner crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def itinerary_planner_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["itinerary_planner_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def accommodation_finder_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["accommodation_finder_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def budget_management_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["budget_management_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def activity_recommendation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["activity_recommendation_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def transportation_optimization_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["transportation_optimization_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def local_expert_ai_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["local_expert_ai_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def weather_and_conditions_monitoring_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["weather_and_conditions_monitoring_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def flight_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["flight_agent"],
            verbose=True,
        )

    @task
    def itinerary_planner_task(self) -> Task:
        return Task(
            config=self.tasks_config["itinerary_planner_task"],
            output_file="output/itinerary_planner_task.md",
        )

    @task
    def accommodation_finder_task(self) -> Task:
        return Task(
            config=self.tasks_config["accommodation_finder_task"],
            output_file="output/accommodation_finder_task.md",
        )

    @task
    def budget_management_task(self) -> Task:
        return Task(
            config=self.tasks_config["budget_management_task"],
            output_file="output/budget_management_task.md",
        )

    @task
    def activity_recommendation_task(self) -> Task:
        return Task(
            config=self.tasks_config["activity_recommendation_task"],
            output_file="output/activity_recommendation_task.md",
        )

    @task
    def transportation_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config["transportation_optimization_task"],
            output_file="output/transportation_optimization_task.md",
        )

    @task
    def local_expert_ai_task(self) -> Task:
        return Task(
            config=self.tasks_config["local_expert_ai_task"],
            output_file="output/local_expert_ai_task.md",
        )

    @task
    def weather_conditions_monitoring_task(self) -> Task:
        return Task(
            config=self.tasks_config["weather_conditions_monitoring_task"],
            output_file="output/weather_conditions_monitoring_task.md",
        )

    @task
    def flight_task(self) -> Task:
        return Task(
            config=self.tasks_config["flight_task"],
            output_file="output/flights.txt",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )