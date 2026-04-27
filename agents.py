from crewai import Agent
from tools import yt_tool
import os
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "sk-proj-1111"

llm = ChatOpenAI(
    model="deepseek-r1:8b",
    base_url="http://localhost:11434/v1",
    api_key="sk-proj-1111"
)

# Senior blog researcher
blog_researcher = Agent(
    role='blog researcher from youtube videos',
    goal='get the relevant video content from the topic {topic} from youtube channel',
    verbose=True,
    memory=True,
    backstory=("Everything is a blog, and I'm a senior blog researcher. I love to write blogs about anything related to technology or science. I have been doing this for years now and I am very good"),
    tools=[yt_tool],
    allow_delegation=True,
    llm=llm
)

# Senior blog writer
blog_writer = Agent(
    role='blog writer',
    goal='Narrate the tech stories from the {topic} in a way that is easy to understand',
    verbose=True,
    memory=True,
    backstory=("Everything is a blog, and I'm a senior blog writer. I love to write blogs about anything related to technology or science. I have been doing this for years now and I am very good"),
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm
)