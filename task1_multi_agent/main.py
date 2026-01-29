from orchestrator import app
from tools import get_company_data
import os 


NEWS_API_KEY = os.getenv('NEWS_API')
ALPHA_API_KEY = os.getenv('ALPHA_VANTAGE')
GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY3')

if __name__ == "__main__":
    result = app.invoke({
        "company": "Tata Consultancy Services",
        "tool": get_company_data
    })

    print("\n===== FINAL COMPANY INTELLIGENCE REPORT =====\n")
    print(result["final_report"])