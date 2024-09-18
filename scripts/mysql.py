# pip install sqlalchemy pymysql

from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os 

load_dotenv()

username = os.getenv('username')
password = os.getenv('password')
host = os.getenv('hostaddress')

# Define your connection string for MySQL
DATABASE_URL = f'mysql+pymysql://{username}:{password}@{host}:3306/life'

# Step 1: Create the engine (connects to the remote MySQL database)
engine = create_engine(DATABASE_URL)

# Step 2: Test the connection by querying the MySQL version
with engine.connect() as connection:
    result = connection.execute("SELECT VERSION();")
    version = result.fetchone()
    print(f"MySQL Database version: {version[0]}")

# Step 3: Create some fake data
data = {
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [30, 25, 35]
}

df = pd.DataFrame(data)

# Step 4: Save the DataFrame to the MySQL database
df.to_sql('users', engine, if_exists='replace', index=False)

# Step 5: Query the table to verify the data
query = 'SELECT * FROM users'
result_df = pd.read_sql(query, engine)

# Step 6: Display the result
print(result_df)
