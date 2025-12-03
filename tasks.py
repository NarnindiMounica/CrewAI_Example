from crewai import Task
from tools import youtube_tool
from agents import blog_researcher, blog_writer
 
#Defining tasks

research = Task(
    description='''From the given channel, identify the video content which is suitable for the given topic {topic}.
                    Get detailed information about the video from the channel.''',
    expected_output='A comprehensive 3 paragraph long report based on the {topic} of the video content',
    agent=blog_researcher,
    tools=[youtube_tool]
)

write = Task(
    description='Get the info from the youtube channel on the topic {topic}',
    expected_output='A blog post formatted in markdown with engaging, informative, and accessible content, avoiding complex jargon.',
    agent=blog_writer,
    tools=[youtube_tool],
    output_file='blog-posts/new_post.md'  # The final blog post will be saved here
)

