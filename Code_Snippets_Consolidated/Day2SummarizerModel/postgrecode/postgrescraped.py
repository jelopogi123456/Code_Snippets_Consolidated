import json
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Load JSON file
with open('C:\\Users\\MARK3\\Downloads\\scraped_articles.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert JSON to DataFrame
df = pd.DataFrame(data)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="articles",
    user="postgres",
    password="interntest123",  # Replace with the password you set during PostgreSQL installation
    host="localhost",
    port="5432"
)

# Insert data into the 'scraped_articles' table
with conn.cursor() as cursor:
    insert_query = "INSERT INTO scraped_articles (title, author, date, content, source) VALUES %s"
    execute_values(cursor, insert_query, [tuple(x) for x in df.to_records(index=False)])
    conn.commit()

# Close the connection
conn.close()
