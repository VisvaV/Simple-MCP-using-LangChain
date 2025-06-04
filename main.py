import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool, initialize_agent
from langchain.agents.agent_types import AgentType
from client import run_tool_sync
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.3)

def mcp_tool(query: str) -> str:
    return run_tool_sync(query)

tools = [
    Tool(
        name="MCP Process Query Tool",
        func=mcp_tool,
        description="Uses MCP to route a query to the server's registered tool."
    )
]

agent = initialize_agent(tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

if __name__ == "__main__":
    query = "Use the tool to process a question about climate change."
    print("User Query:", query)
    response = agent.run(query)
    print("Agent Response:", response)
