from langchain.tools import DuckDuckGoSearchRun
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
from agents import TradingCompanyAgents
from dotenv import load_dotenv
from tasks import FinTechTasks
from textwrap import dedent
from decouple import config
import os


search_tool = DuckDuckGoSearchRun()

# Load the environmental variables
# OPENAI_API_KEY, OPENAI_ORGANIZATION_ID
load_dotenv()

# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class FinTechCrew:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = TradingCompanyAgents()
        tasks = FinTechTasks()

        # Define your custom agents and tasks here
        news_gatherer_agent = agents.news_data_gatherer_agent()
        public_gatherer_agent = agents.public_data_gatherer_agent()
        sentiment_analyse_agent = agents.sentiment_analyzer_agent()
        trading_decision_agent = agents.trading_decision_agent()

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.obtain_latest_data_from_market(
            news_gatherer_agent,
        )
        custom_task_2 = tasks.obtain_latest_data_from_market(
            public_gatherer_agent,
        )
        custom_task_3 = tasks.obtain_latest_data_from_market(
            sentiment_analyse_agent,
        )
        custom_task_4 = tasks.determine_best_companies_positions(
            trading_decision_agent,
        )


        # Define your custom crew here
        crew = Crew(
            agents=[news_gatherer_agent, public_gatherer_agent, sentiment_analyse_agent, trading_decision_agent],
            tasks=[custom_task_1, custom_task_2, custom_task_3, custom_task_4],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("-------------------------------")
    var1 = dedent("""""")
    var2 = dedent("""""")

    fintech_crew = FinTechCrew(var1, var2)
    result = fintech_crew.run()
    print("\n\n########################")
    print(result)
