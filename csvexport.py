import pyodbc
import csv
import urllib

# Set up a connection to the SQL Server database

# Connection details
username = "sa"
password = "pass@word1"
server = "localhost"
database_name = "morse"
driver = "ODBC+Driver+18+for+SQL+Server"

# Create a URL-encoded connection string
params = urllib.parse.quote_plus(f"DRIVER={{{driver}}};SERVER={server};DATABASE={database_name};UID={username};PWD={password};TrustServerCertificate=yes;Encrypt=yes")
connectionString=f"mssql+pyodbc:///?odbc_connect={params}"

connection = pyodbc.connect(connectionString)

# Open a cursor for executing SQL queries
cursor = connection.cursor()

# Execute a SQL query to select data from the table you want to export
cursor.execute('SELECT * FROM RadioMessages')

# Fetch the data from the cursor
data = cursor.fetchall()

# Close the cursor and the database connection
cursor.close()
connection.close()

# Open a CSV file for writing the data to
with open('radiomessages.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the header row of the CSV file
    writer.writerow([column[0] for column in cursor.description])

    # Write each row of data to the CSV file
    for row in data:
        writer.writerow(row)
