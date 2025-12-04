from crewai import Crew, Process
from agents import blog_researcher, blog_writer
from tasks import research, write

#forming the tech-focused crew with some enhanced configurations

crew= Crew(
    agents=[blog_researcher, blog_writer],
    tasks=[research, write],
    process=Process.sequential, #Optional: sequential task execution is default
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True,
    verbose = True)

result = crew.kickoff(inputs={'topic':'https://docs.crewai.com/en/introduction'})
print(result)
