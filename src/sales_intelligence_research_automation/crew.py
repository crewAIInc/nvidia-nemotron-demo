import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool
)





@CrewBase
class SalesIntelligenceResearchAutomationCrew:
    """SalesIntelligenceResearchAutomation crew"""


    @agent
    def company_research_specialist(self) -> Agent:

        return Agent(
            config=self.agents_config["company_research_specialist"],


            tools=[				SerperDevTool()],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,


            max_execution_time=None,
            llm=LLM(
                model="nvidia_nim/nvidia/nemotron-3-super-120b-a12b",
                temperature=0.7,

            ),

        )

    @agent
    def hubspot_data_analyst(self) -> Agent:

        return Agent(
            config=self.agents_config["hubspot_data_analyst"],


            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,

            apps=[
                    "hubspot/search_contacts",
                    ],


            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,

            ),

        )

    @agent
    def email_history_analyst(self) -> Agent:

        return Agent(
            config=self.agents_config["email_history_analyst"],


            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,

            apps=[
                    "google_gmail/fetch_emails",
                    ],


            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                temperature=0.7,

            ),

        )

    @agent
    def sales_intelligence_report_writer(self) -> Agent:

        return Agent(
            config=self.agents_config["sales_intelligence_report_writer"],


            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,


            max_execution_time=None,
            llm=LLM(
                model="nvidia_nim/nvidia/nemotron-3-super-120b-a12b",
                temperature=0.7,

            ),

        )



    @task
    def research_prospect_and_company(self) -> Task:
        return Task(
            config=self.tasks_config["research_prospect_and_company"],
            markdown=False,


        )

    @task
    def analyze_hubspot_data(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_hubspot_data"],
            markdown=False,


        )

    @task
    def analyze_email_history(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_email_history"],
            markdown=False,


        )

    @task
    def create_sales_intelligence_report(self) -> Task:
        return Task(
            config=self.tasks_config["create_sales_intelligence_report"],
            markdown=False,


        )


    @crew
    def crew(self) -> Crew:
        """Creates the SalesIntelligenceResearchAutomation crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )
