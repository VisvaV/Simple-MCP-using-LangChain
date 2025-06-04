# main.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from client import ToolClient
from dotenv import load_dotenv

load_dotenv()

# Setup LangChain LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.3)

# Setup tool
tool_client = ToolClient()

def tool_func(query: str) -> str:
    return tool_client.run_tool(query)

tools = [
    Tool(
        name="Simple Tool",
        func=tool_func,
        description="Calls a simple server that processes a query and returns a message."
    )
]

# Initialize the agent with LangChain
agent = initialize_agent(tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

# Run the agent
if __name__ == "__main__":
    query = "Use the tool to process a question about climate change."
    print("User Query:", query)
    response = agent.run(query)
    print("Agent Response:", response)