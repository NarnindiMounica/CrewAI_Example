from crewai import Task
from tools import browser_tool
from agents import blog_researcher, blog_writer
 
#Defining tasks

research = Task(
    description='''From the given webpage, identify the article content from the given webpage {page}.
                    Get detailed information about the context from the webpage''',
    expected_output='A comprehensive 3 paragraph long report based on the {page} of the website.',
    agent=blog_researcher,
    tools=[browser_tool]
)

write = Task(
    description='Get the info from the website of page {page}',
    expected_output='A blog post formatted in markdown with engaging, informative, and accessible content, avoiding complex jargon.',
    agent=blog_writer,
    tools=[browser_tool],
    output_file='blog-posts/new_post.md'  # The final blog post will be saved here
)

