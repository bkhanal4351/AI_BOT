from config import OPENAI_API_KEY
from db_connection import db
from langchain_experimental.sql import SQLDatabaseChain
from langchain.chat_models import ChatOpenAI
import sys
import os

# Ensure the script can find db_connection.py
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


# Initialize AI model
llm = ChatOpenAI(model="gpt-4", openai_api_key=OPENAI_API_KEY, temperature=0)

# Create database chain
db_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True)


def ask_bot(user_query):
    """Processes user input and returns database results."""
    return db_chain.run(user_query)


def get_db_response(user_query):
    """Processes user input and returns database results."""
    return db_chain.run(user_query)


if __name__ == "__main__":
    while True:
        query = input("Ask me something: ")
        if query.lower() == "exit":
            break
        response = ask_bot(query)
        print(response)
