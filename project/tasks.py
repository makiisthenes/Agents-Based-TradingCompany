from crewai import Task
from textwrap import dedent


class FinTechTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def obtain_latest_data_from_market(self, agent):
        return Task(
            description=dedent(
                f"""
            At the start of the day, we must obtain the latest data in order to make the best trading decisions. We want to know which companies are currently being talked about, 
            this includes what the news is saying, the sources mentioning this, the different headlines as well as how relevant this information is.
            
            
            {self.__tip_section()}
    
            Make sure to use the most recent data as possible.

        """
                # Use this variable: {var1}
                # And also this variable: {var2}
            ),
            agent=agent,
        )

    def determine_best_companies_positions(self, agent):
        return Task(
            description=dedent(
                f""" Understanding the news and the effect it has on the stock market is crucial. We need to 
                determine the best companies to open and close positions for the day. If we know something is going 
                to happen that will affect the stock price, we need to act on it. Provide an buy or sell order for 
                specific companies that will lead to predicted profitability, as well as some reasoning for such event.
                                       
            {self.__tip_section()}

            Make sure to do something else.
        """
            ),
            agent=agent,
        )
