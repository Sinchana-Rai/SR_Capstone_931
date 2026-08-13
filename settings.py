import os
from dotenv import load_dotenv
 
# Load environment variables
load_dotenv()
 
# Get API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
 
# Model 
MODEL_ID = "mixtral-8x7b-32768"
 
print("Configuration loaded successfully!")
print(f"API Key present: {bool(GROQ_API_KEY)}")
print(f"Model: {MODEL_ID}")