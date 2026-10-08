import os
from dotenv import load_dotenv

print("TEST.PY IS RUNNING")

# Load environment variables
load_dotenv()

# Get Groq API key
api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print("GROQ KEY FOUND")
else:
    print("GROQ KEY NOT FOUND")