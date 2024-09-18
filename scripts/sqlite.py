import pandas as pd
import sqlite3

# Step 1: Create a connection to SQLite database
conn = sqlite3.connect('test_database.db')

# Step 2: Create a Pandas DataFrame
df = pd.read_csv('https://data.cdc.gov/resource/it4f-frdc.csv')
df['sex'].value_counts()

# Step 3: Save the DataFrame to the SQLite database
df.to_sql('life_expec', conn, if_exists='replace', index=False)

# Step 4: Query the table to verify the data
query_1 = 'SELECT area, sex, leb FROM life_expec'
result_df = pd.read_sql(query_1, conn)

# Step 5: Display the result
print(result_df)

# Close the connection
conn.close()
