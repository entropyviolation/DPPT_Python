import os
import psycopg2

# Set the DATABASE_URL variable to the connection string
DATABASE_URL = os.environ.get('DATABASE_URL')

# Connect to the PostgreSQL database
conn = psycopg2.connect(DATABASE_URL)

# Create a cursor object
cur = conn.cursor()

# Create the chat_data table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS chat_data (
    id SERIAL PRIMARY KEY,
    responses TEXT,
    analysis TEXT
)
""")

# Commit the changes and close the cursor
conn.commit()
cur.close()

# Don't forget to close the connection when you're done
# conn.close()
