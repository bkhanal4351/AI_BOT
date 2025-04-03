from langchain.sql_database import SQLDatabase
import os

# Set your database connection string (PostgreSQL, MySQL, SQLite, etc.)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///example.db")

# Initialize the database connection
db = SQLDatabase.from_uri(DATABASE_URL)
