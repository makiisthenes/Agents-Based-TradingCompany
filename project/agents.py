import os

from crewai import Agent
from textwrap import dedent
from dotenv import load_dotenv
from langchain.agents import load_tools
from langchain.tools import BraveSearch
from langchain_openai import ChatOpenAI
from langchain.llms import OpenAI, Ollama
from tools.fin_sentiment_tools import SentimentTools
from langchain_community.tools.google_trends import GoogleTrendsQueryRun
from langchain_community.tools.google_finance import GoogleFinanceQueryRun
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchResults
from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
from langchain_community.utilities.alpha_vantage import AlphaVantageAPIWrapper
from langchain_community.utilities.google_trends import GoogleTrendsAPIWrapper
from langchain_community.utilities.google_finance import GoogleFinanceAPIWrapper
from langchain_community.utilities.duckduckgo_search import DuckDuckGoSearchAPIWrapper

# We are a Trading Company, named Maki. I would like to define a few agents, whose roles will be to make trading
# decisions for each day. We will have a few agents, and each agent will have a different role, and backstory. First,
# we will obtain the data for the day, which includes the news, the current stock prices, and the current public
# sentiment. We will then use this data to analyze the company's positions through their filings. We will
# then use this to make a decision on which stocks to buy and short for the day, opening and closing positions.

load_dotenv()
# Brave and Duckduckgo Tool Initialisation
brave_search = BraveSearch.from_api_key(api_key=os.getenv("BRAVE_SEARCH_API_KEY"), search_kwargs={"count": 3})
wrapper = DuckDuckGoSearchAPIWrapper(region="en", time="d", max_results=10)
ddg_search = DuckDuckGoSearchResults(api_wrapper=wrapper, source="news")
google_search_tool = GoogleFinanceQueryRun(api_wrapper=GoogleFinanceAPIWrapper())
google_trend_tool = GoogleTrendsQueryRun(api_wrapper=GoogleTrendsAPIWrapper())


class TradingCompanyAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.6)
        self.Ollama = Ollama(model="openhermes")

    def news_data_gatherer_agent(self):
        """
        This agent is responsible for gathering the data for the day, which includes the news, the current stock prices, for data analysis to format.
        This agent has access to tools to obtain such data, including:
        - Yahoo Finance News
        - Alpha Vantage API
        - Google Search Tool
        - Google Trend Tool
        """
        return Agent(
            role="Data Gatherer Agent",
            backstory=dedent(f"""This agent has a background in data analytics, has understanding of the news and the effect it has on the stock market."""),
            goal=dedent(f"""This agent is responsible for gathering the data for the day, which includes the news, the current stock prices, and the current public sentiment."""),
            tools=[YahooFinanceNewsTool(), AlphaVantageAPIWrapper()],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )

    def public_data_gatherer_agent(self):
        """
        This agent is responsible for gathering publicly available data which specifically includes social media data and public search forums.

        """
        return Agent(
            role="Public Data Gatherer Agent",
            backstory=dedent(f"""This agent has a background in data analytics, has understanding of the news and the effect it has on the stock market."""),
            goal=dedent(f"""This agent is responsible for gathering publicly available data which specifically includes social media data and public search forums."""),
            tools=[brave_search, ddg_search, google_search_tool, google_trend_tool] + load_tools(["google_finance"], llm=self.Ollama),
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )

    def sentiment_analyzer_agent(self):
        return Agent(
            role="Sentiment Analyzer Agent",
            backstory=dedent(f"""This agent has a background in sentiment analysis, and has understanding of the news and the effect it has on the stock market."""),
            goal=dedent(f"""This agent is responsible for analyzing the sentiment of the news, and the effect it has on the stock market."""),
            tools=[SentimentTools.get_simple_sentiment_analysis, SentimentTools.get_strong_sentiment_analysis],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )

    def trading_decision_agent(self):
        """
        Based on the data gathered, and sentiment analysis, this agent is responsible for making trading decisions for the day.
        """
        return Agent(
            role="Trading Decision Agent",
            backstory=dedent(f"""This agent has a background in trading, and has understanding of the news and sentiment effects the market, it knows which stocks to pick to improve the companies capital position."""),
            goal=dedent(f"""Based on the data gathered, and sentiment analysis, this agent is responsible for making trading decisions for the day ."""),
            tools=[],
            allow_delegation=False,
            verbose=True,
            llm=self.Ollama,
        )

