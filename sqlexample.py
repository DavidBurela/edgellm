### Required setup ###
# pip install openai langchain sqlalchemy pyodbc
# pip install llama-cpp-python # ONLY for llamacpp
# sudo apt-get install unixodbc-dev #for DB connections
# install SQL ODBC (msodbcsql18):  https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server

# Background: Documentation that got me started: https://python.langchain.com/en/latest/modules/agents/toolkits/examples/sql_database.html

from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor

import urllib

# Connection details
username = "sa"
password = "pass@word1"
server = "localhost"
database_name = "morse"
driver = "ODBC+Driver+18+for+SQL+Server"

# Create a URL-encoded connection string
params = urllib.parse.quote_plus(
    f"DRIVER={{{driver}}};SERVER={server};DATABASE={database_name};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=yes"
)
connectionString=f"mssql+pyodbc:///?odbc_connect={params}"

db = SQLDatabase.from_uri(connectionString)
toolkit = SQLDatabaseToolkit(db=db)

# Invoke the agent
agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True
)

agent_executor.run("Describe the RadioMessages table")
#agent_executor.run("How many people were injured in the anus? do not limit to 10")
#agent_executor.run("How many people were injured in total?")
