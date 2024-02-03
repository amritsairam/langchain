import os 
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
openai_api_key = os.getenv("OPENAI_API_KEY")

from langchain.prompts import PromptTemplate

prompt_template = PromptTemplate.from_template(
    "you are an expert financial advisor, give the user more information about {topic}"
)
prompt_template.format(adjective="funny", content="chickens")