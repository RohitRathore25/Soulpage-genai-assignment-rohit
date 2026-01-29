import streamlit as st
from orchestrator import app
from tools import get_company_data
import os 
import google.generativeai as genai

NEWS_API_KEY = os.getenv('NEWS_API')
ALPHA_API_KEY = os.getenv('ALPHA_VANTAGE')
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY3')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.5-flash-lite',
                              generation_config={'temperature':0.2})

st.set_page_config(page_title="Company Intelligence Agent")

st.title("Company Intelligence Agent (LangGraph + Gemini)")
st.write("Multi-Agent System with real API data")

company = st.text_input("Enter company name", "Tata Consultancy Services")

if st.button("Generate Report"):
    with st.spinner("Agents collaborating..."):
        result = app.invoke({
            "company": company,
            "tool": get_company_data
        })

    st.subheader("Intelligence Report")
    st.write(result["final_report"])
