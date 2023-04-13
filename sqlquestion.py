### Required setup ###
# pip install openai langchain==0.0.136 sqlalchemy pyodbc
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

#### SQL CONNECTION ####
# Connection details
username = "sa"
password = "L4YZq6PEmyP$"
server = "20.213.174.28"
database_name = "morse"
driver = "ODBC+Driver+18+for+SQL+Server"

# Create a URL-encoded connection string
params = urllib.parse.quote_plus(f"DRIVER={{{driver}}};SERVER={server};DATABASE={database_name};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=yes")
connectionString=f"mssql+pyodbc:///?odbc_connect={params}"

db = SQLDatabase.from_uri(connectionString)
toolkit = SQLDatabaseToolkit(db=db)


### Cloud
# model = OpenAI(temperature=0)

### Edge
from langchain.llms import LlamaCpp
# model = LlamaCpp(model_path="./models/gpt4all-lora-quantized-new.bin", n_ctx=2048, verbose=True, n_threads=16)
# model = LlamaCpp(model_path="./models/ggml-vicuna-7b-4bit-rev1.bin", n_ctx=2048, verbose=True, n_threads=16)
model = LlamaCpp(model_path="./models/ggml-vicuna-13b-4bit-rev1.bin", n_ctx=4096, verbose=True, n_threads=16, max_tokens=1024)

# legacy edge
#from langchain.llms import GPT4All
# model = GPT4All(model="./models/ggml-vicuna-13b-4bit-rev1.bin", n_ctx=2048, verbose=True, n_threads=16)

# Invoke the agent
agent_executor = create_sql_agent(
    llm=model,
    toolkit=toolkit,
    verbose=True
)

agent_executor.run("Describe the RadioMessages table")
agent_executor.run("In the RadioMessages table, how many people suffered a wound?") #local
# agent_executor.run("How many people were injured in total?")
# agent_executor.run("How many people suffered a wound?") #OpenAI
# agent_executor.run("Give me a row from RadioMessages")
