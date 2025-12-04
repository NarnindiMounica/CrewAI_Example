import os
from crewai import Agent
from tools import browser_tool

from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

groq_api_key= os.getenv('GROQ_API_KEY')


model = ChatGroq(model="llama-3.1-8b-instant", api_key=groq_api_key)

#create a senior blog content researcher

blog_researcher = Agent(
    role="Web Researcher",
    goal="Get the relevant information from given website {page} in reference to data science and generative ai",
    backstory="Senior Web Researcher who is well experienced, an expert in understanding details from given website related to data science and generative ai. ",
    verbose=True,
    memory=True,
    tools=[browser_tool],
    llm=model, 
    allow_delegation=True
)

#create agent for blog writer agent for browser base load tool.

blog_writer = Agent(
    role="Blog writer for data science and generative ai",
    goal="Write simple but understandable tech stories about a technology related article in simple and concise fasion. ",
    backstory='''
                With a flair for simplifying complex topics, you craft
                engaging narratives that captivate and educate, bringing new
                discoveries to light in an accessible manner''',
    verbose=True,
    memory=True,
    tools=[browser_tool],
    llm=model,
    allow_delegation=False
)

