from crewai import Task
from agents import blog_researcher, blog_writer
from tools import yt_tool

researcher_task = Task(
    description="Research the topic {topic} and gather relevant information from youtube videos",
    agent=blog_researcher,
    tools=[yt_tool],
    expected_output="A comprehensive research report on the topic {topic} with relevant video content from youtube channel"
)

writer_task = Task(
    description="Write a blog post based on the research report on the topic {topic}",
    agent=blog_writer,
    tools=[yt_tool],
    expected_output="A well-structured blog post on the topic {topic} incorporating the research findings"
)

