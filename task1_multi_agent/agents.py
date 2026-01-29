import os
from typing import Dict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import google.generativeai as genai


NEWS_API_KEY = os.getenv('NEWS_API')
ALPHA_API_KEY = os.getenv('ALPHA_VANTAGE')
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY3')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-lite',
                              generation_config={'temperature':0.2})


def data_collector_agent(state: Dict):
    """
    Agent 1: Fetches real-world data using tools
    """
    company = state["company"]
    tool = state["tool"]

    company_data = tool(company)

    return {
        "company_data": company_data
    }


def analyst_agent(state: Dict):
    """
    Agent 2: Analyzes data using Gemini
    """
    company_data = state["company_data"]

    prompt = ChatPromptTemplate.from_template("""
    You are a financial analyst.

    Company Data:
    {company_data}

    Generate:
    - Market summary
    - Key insights
    - Potential risks
    """)

    response = model.generate_content(
        prompt.format(company_data = state['company_data'])
    )
    
    return {'final_report': response.text}
