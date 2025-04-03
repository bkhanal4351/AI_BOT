import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve values
DB_URI = os.getenv("DB_URI")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
