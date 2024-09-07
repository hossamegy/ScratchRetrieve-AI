from agent_from_scratch import SimpleAgent
from retriever import Retriver
from reAct_prompt import reActPrompt
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

course_info_retriever, agent_info_retriever, user_info_retriever = Retriver(
    r"", # add domain pdf
    r"", # add info pdf about agent
    r"" # add user pdf about agent
).create()

known_actions = {
    "course_info_retriever": course_info_retriever,
    "agent_info_retriever": agent_info_retriever,
    "user_info_retriever": user_info_retriever
}

model_name = "gemini-1.5-flash-latest" 
prompt = reActPrompt()

agent = SimpleAgent(
    model_name=model_name,
    known_actions=known_actions,
    system=prompt
)

if __name__ == '__main__':
    agent.query("what is your name", max_turns=10)