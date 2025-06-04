# client.py
import requests

class ToolClient:
    def __init__(self, base_url="http://localhost:5001"):
        self.base_url = base_url

    def run_tool(self, query):
        response = requests.post(f"{self.base_url}/tool", json={"query": query})
        if response.status_code == 200:
            return response.json()["result"]
        else:
            return "Tool execution failed"