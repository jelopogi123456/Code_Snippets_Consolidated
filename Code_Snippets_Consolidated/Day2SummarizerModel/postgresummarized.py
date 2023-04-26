import json
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Function to convert numpy types to native Python types
def convert_numpy_types(value):
    if isinstance(value, (pd.Int64Dtype, pd.Int32Dtype, int)):
        return int(value)
    return value

# Load JSON file
with open('C:\\Users\\MARK3\\Downloads\\summarized_article_intern.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Convert JSON to DataFrame
df = pd.DataFrame(data)

# Select specific columns to insert into the database
df = df[['title', 'author', 'date', 'content', 'summarized_articles']]

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="articles",
    user="postgres",
    password="interntest123",  # Replace with the password you set during PostgreSQL installation
    host="localhost",
    port="5432"
)

# Create the table with the selected columns
with conn.cursor() as cursor:
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS summarized_articles (
        id SERIAL PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT,
        date DATE,
        content TEXT,
        summarized_articles TEXT
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()

# Insert data into the table
with conn.cursor() as cursor:
    insert_query = '''
    INSERT INTO summarized_articles (
        title, author, date, content, summarized_articles
    ) VALUES %s
    '''
    records = [tuple(convert_numpy_types(x) for x in row) for row in df.to_records(index=False)]
    execute_values(cursor, insert_query, records)
    conn.commit()

# Close the connection
conn.close()
