# To install: pip install tavily-python python-dotenv

import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()
client = TavilyClient(os.environ["TAVILY_API_KEY"])
response = client.search(
    query="list the technical jobs with AI for someone with 10 years of engineering leadership",
    search_depth="advanced"
)
print(response)
