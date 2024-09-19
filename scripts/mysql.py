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

# Step 2: Create some fake data
df = pd.read_csv('https://data.cdc.gov/resource/it4f-frdc.csv')

females = df[df['sex'] == 'Female']
males = df[df['sex'] == 'Male']

females['leb'].describe()
males['leb'].describe()

# Step 4: Save the DataFrame to the MySQL database
females.to_sql('female', engine, if_exists='replace', index=False)
males.to_sql('male', engine, if_exists='replace', index=False)

# Step 5: Query the table to verify the data
query = 'SELECT * FROM female'
result_df = pd.read_sql(query, engine)
result_df

# Step 6: Display the result
print(result_df)

query_california_females = 'select * from female where area = "North Carolina"' 
df_ca = pd.read_sql(query_california_females, engine)
df_ca

query_2 = """
SELECT * 
FROM female
WHERE area in("California", "Texas", "North Carolina", "South Carolina")
LIMIT 5;
"""

test = pd.read_sql(query_2, engine)
test


query_3 = """
SELECT * 
FROM female
WHERE leb < 78.0
LIMIT 5;
"""


query_4 = """
SELECT * 
FROM male
WHERE leb < 78.0
LIMIT 5;
"""

query_5 = """
SELECT * 
FROM male
WHERE leb > 75.0
LIMIT 5;
"""

query_6 = """
SELECT * 
FROM female
WHERE leb > 80.0
LIMIT 5;
"""

worst_female = pd.read_sql(query_3, engine)
worst_male = pd.read_sql(query_4, engine)

best_female = pd.read_sql(query_6, engine)
best_male = pd.read_sql(query_5, engine)