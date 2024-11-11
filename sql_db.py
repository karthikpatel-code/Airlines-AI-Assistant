import sqlite3
import pandas as pd
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('Airlines.db')
cursor = conn.cursor()

# SQL statement to create the table schema
def sql_ingest():
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Airlines_data (
        id INTEGER PRIMARY KEY,
        airline_name TEXT NOT NULL,
        departure_date DATETIME NOT NULL
    );
    '''

    # Execute the query
    cursor.execute(create_table_query)



    # Commit changes and close the connection
    conn.commit()

    df_sql_db = pd.read_csv("Airlines_data.csv")
    df_sql_db=df_sql_db[['departure_date', 'airline_name']]
    df_sql_db['date'] = pd.to_datetime(df_sql_db['departure_date'])
    df_sql_db['date'] = df_sql_db['date'].dt.date
    df_sql_db['date'] = pd.to_datetime(df_sql_db['date'])
    df_sql_db['id'] = range(1, len(df_sql_db) + 1)  # starting index at 1

    # Set 'id' as the index
    # df_sql_db.set_index('id', inplace=True)

    try:

        
        # Insert data into an existing table with a specific schema
        for _, row in df_sql_db.iterrows():
            cursor.execute(
                "INSERT INTO Airlines_data (id, airline_name, departure_date) VALUES (?, ?, ?)",
                (row['id'], row['airline_name'], row['departure_date'])
            )
        
        # Commit the transaction
        conn.commit()

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        # Close the connection
        if conn:
            conn.close()




    return "Table 'Airlines_data' created successfully."
