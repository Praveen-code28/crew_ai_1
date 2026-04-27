from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research_task, writer_task  # make sure name matches

crew = Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research_task, writer_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    verbose=True
)

result = crew.kickoff(
    inputs={'topic': 'Deep Learning In-depth Tutorials in 5 Hours With Krish Naik'}
)

print(result)