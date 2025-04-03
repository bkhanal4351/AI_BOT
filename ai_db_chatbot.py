from langchain.chat_models import ChatOpenAI
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from config import OPENAI_API_KEY
from db_connection import db  # Ensure this file properly sets up your DB connection

# Initialize the OpenAI model
llm = ChatOpenAI(model="gpt-4", openai_api_key=OPENAI_API_KEY, temperature=0)

# Create the SQL Database Chain
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)
