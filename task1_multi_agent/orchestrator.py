from typing import TypedDict, Any
from langgraph.graph import StateGraph, END
from agents import data_collector_agent, analyst_agent
import os 

NEWS_API_KEY = os.getenv('NEWS_API')
ALPHA_API_KEY = os.getenv('ALPHA_VANTAGE')
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY3')

class AgentState(TypedDict):
    company: str
    tool: Any
    company_data: dict
    final_report: str


graph = StateGraph(AgentState)

graph.add_node("collector", data_collector_agent)
graph.add_node("analyst", analyst_agent)

graph.set_entry_point("collector")
graph.add_edge("collector", "analyst")
graph.add_edge("analyst", END)

app = graph.compile()
