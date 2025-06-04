import asyncio
from mcp.client.stdio import stdio_client
from mcp import ClientSession, StdioServerParameters

class ToolClient:
    def __init__(self, server_script_path="server.py"):
        self.server_script_path = server_script_path

    async def run_tool(self, query):
        server_params = StdioServerParameters(
            command="python",
            args=[self.server_script_path],
            env=None
        )

        async with stdio_client(server_params) as client:
            tools = await client.list_tools()
            if "process_query" in tools:
                result = await client.call_tool("process_query", {"query": query})
                return result
            else:
                return "Tool not found"

def run_tool_sync(query):
    client = ToolClient()
    return asyncio.run(client.run_tool(query))
