from mcp.server.fastmcp import FastMCP

mcp = FastMCP("LangChainMCPServer")

@mcp.tool()
def process_query(query: str) -> str:
    """Processes the query and returns a response."""
    return f"Tool executed successfully for query: {query}"

if __name__ == "__main__":
    mcp.run(transport="stdio")
