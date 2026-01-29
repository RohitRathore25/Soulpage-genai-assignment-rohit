# Soulpage-genai-assignment-rohit
End-to-end GenAI assignment showcasing LangGraph-based multi-agent orchestration and a conversational AI bot with memory and external tools.


GitHub Repository Contents

This repository includes the following deliverables as required:

1. Source Code

Complete implementation of the multi-agent system using LangGraph

Modular and well-structured Python files for:

Agents

Orchestrator/controller

External tool integrations

Optional Streamlit UI to interact with the orchestrator agent

2. Architecture / Flow Description

The system follows a multi-agent orchestration flow:

The user provides a company name as input.

The orchestrator agent initializes and controls the workflow.

The Data Collector Agent:

Fetches real-time company news using NewsAPI

Fetches financial and stock data using Alpha Vantage

The collected data is stored in a shared state managed by LangGraph.

The Analyst Agent:

Consumes the shared data

Uses a Large Language Model (Gemini) to analyze and summarize insights

The orchestrator combines outputs and returns a final company intelligence report to the user.

This flow ensures clear separation of concerns, tool-augmented reasoning, and contextual data sharing between agents.

3. Instructions to Run

Step 1: Install dependencies

pip install -r requirements.txt


Step 2: Set environment variables

NEWS_API  = d342f4123dbb4c518bf7818f78a6b215

ALPHA_VANTAGE = KC4A56DNCOF5Q26E

Step 3: Run the application

python task1_multi_agent/main.py


Optional: Run Streamlit UI

streamlit run task1_multi_agent/app.py

4. Bonus: Reproducibility Notebook

A Jupyter Notebook is included for reproducibility:

task1_multi_agent/task1_demo.ipynb


The notebook demonstrates:

Agent execution flow

Tool calls

Final output generation

Summary

All required deliverables are included:

Source code

Architecture / flow description

Clear run instructions

Bonus .ipynb notebook for reproducibility


## 🔗 Links

- **GitHub Repository:** https://github.com/RohitRathore25/Soulpage-genai-assignment-rohit
- **Live Demo (Streamlit App):** https://soulpage-genai-assignment-rohit-b9vfcrhzmzpe5wbikxajji.streamlit.app/
