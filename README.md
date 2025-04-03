# AI-DB Chatbot

## 🚀 Project Overview

This AI-powered chatbot allows users to input queries, which the bot processes by generating SQL queries and retrieving results from a database. It integrates **LangChain, OpenAI, SQLAlchemy, and FastAPI** to provide a seamless user experience.

## 📌 Features

- **Natural Language Processing (NLP)** using OpenAI API.
- **Database Querying** with SQLAlchemy.
- **FastAPI Backend** for handling requests.
- **LangChain Integration** for intelligent query generation.
- **Secure Environment Configuration** using `.env` file.

---

## 🛠️ Setup & Installation

```bash
# 1️⃣ Clone the Repository
git clone https://github.com/YOUR-USERNAME/ai-db-chatbot.git
cd ai-db-chatbot

# 2️⃣ Set Up a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate    # For Windows

# 3️⃣ Install Dependencies
pip install -r requirements.txt

# 4️⃣ Configure Environment Variables
# Create a .env file in the project root and add:
echo "OPENAI_API_KEY=your-api-key" > .env
echo "DATABASE_URL=postgresql://user:password@localhost/dbname" >> .env

# 5️⃣ Run the Application
uvicorn chatbot:app --reload


#🔄 How It Works
 1. User Inputs a Query → The chatbot processes the request.
 2. AI Generates an SQL Query → LangChain converts natural language into SQL.
 3. Database Query Execution → SQLAlchemy fetches the results.
 4. Response Formatting → The bot returns results in a structured format.

The API will be available at:

➡️ http://127.0.0.1:8000

📡 API Endpoints

POST /query - Ask the chatbot a question

Request Body:

