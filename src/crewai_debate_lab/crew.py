from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.llm import LLM
import os


@CrewBase
class DebateCrew:
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    def _llm(self) -> LLM:
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")

        return LLM(
            model="gpt-4o-mini",
            api_key=api_key
        )

    @agent
    def debater(self) -> Agent:
        return Agent(
            config=self.agents_config["debater"],
            llm=self._llm(),
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config["judge"],
            llm=self._llm(),
            verbose=True
        )

    @task
    def propose(self) -> Task:
        return Task(config=self.tasks_config["propose"])

    @task
    def oppose(self) -> Task:
        return Task(config=self.tasks_config["oppose"])

    @task
    def decide(self) -> Task:
        return Task(config=self.tasks_config["decide"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
