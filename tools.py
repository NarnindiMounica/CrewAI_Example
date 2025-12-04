import os

from dotenv import load_dotenv
load_dotenv()

browserbase_api_key = os.getenv("BROSWERBASE_API_KEY")
from crewai_tools import BrowserbaseLoadTool

browser_tool=BrowserbaseLoadTool(api_key= browserbase_api_key)