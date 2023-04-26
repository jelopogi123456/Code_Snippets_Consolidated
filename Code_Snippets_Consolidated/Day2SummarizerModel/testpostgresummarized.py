import psycopg2
import pandas as pd

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="articles",
    user="postgres",
    password="interntest123",
    host="localhost",
    port="5432"
)

# Query the 'scraped_articles' table
query = "SELECT * FROM summarized_articles;"
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Print the results
print(df)