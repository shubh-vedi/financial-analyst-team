from crewai import Agent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from langchain_openai import ChatOpenAI

class FinancialCrewAgents:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0.5)

    def financial_researcher(self):
        return Agent(
            role='Financial Researcher',
            goal='Gather and analyze financial data including SEC filings and earnings reports.',
            backstory="""You are an expert financial researcher with a keen eye for detail. 
            You specialize in digging through SEC filings and earnings calls to find the data that matters.""",
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            llm=self.llm,
            verbose=True,
            memory=True
        )

    def competitor_analyst(self):
        return Agent(
            role='Competitor Analyst',
            goal='Analyze the competitive landscape and identify key rivals and their strengths/weaknesses.',
            backstory="""You are a strategic thinker who understands market dynamics. 
            You can identify who the real competitors are and where they stand in the market.""",
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            llm=self.llm,
            verbose=True,
            memory=True
        )

    def sentiment_analyst(self):
        return Agent(
            role='Sentiment Analyst',
            goal='Analyze market sentiment from news, social media, and analyst ratings.',
            backstory="""You are an expert in behavioral finance and market psychology. 
            You read between the lines of news articles and social media trends to gauge underlying sentiment.""",
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            llm=self.llm,
            verbose=True,
            memory=True
        )

    def investment_writer(self):
        return Agent(
            role='Investment Writer',
            goal='Synthesize research into a comprehensive, structured investment report.',
            backstory="""You are a seasoned investment writer who can tell a compelling story with data. 
            You take complex financial analysis and turn it into clear, actionable investment memos.""",
            llm=self.llm,
            verbose=True,
            memory=True,
            allow_delegation=True 
        )
