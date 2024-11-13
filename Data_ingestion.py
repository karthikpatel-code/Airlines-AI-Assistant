import pandas as pd
import uuid
import chromadb
from openai import OpenAI
from sql_db import sql_ingest
import os
import json
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key = openai_api_key)
chroma_root = r"chromadb"
os.makedirs(os.path.join(os.getcwd(),chroma_root),exist_ok =True)




chroma_client = chromadb.PersistentClient(path = chroma_root)
col_name = "Airlines_data"
chroma_col = chroma_client.get_or_create_collection(name = col_name)



#### Data cleaning script ###

df = pd.read_csv(r"Flight Bookings.csv")
df1 = pd.read_csv(r"Airline ID to Name.csv")

df_merged_1 = pd.merge(df, df1, how = 'left', on = ['airlie_id'])
df_merged = df_merged_1.dropna(how = 'all')

df_merged.rename(columns = {"flght#" : "flight_number", 'departure_dt': 'departure_date', "arrival_dt":"arrival_date", "arrivl_time" : "arrival_time", "dep_time":"departure_time", "passngr_nm" : "passngr_name", "seat_no":"seat_number", "inflight_ent": "inflight_entertainment"}, inplace = True)

df_merged.head(50).to_csv("Airlines_data.csv",index = False)

print('Data cleaning completed.....')

df_sql = df_merged[['departure_date', 'airline_name']]

df_sql['id'] = range(1, len(df_sql) + 1)  # starting index at 1

# Set 'id' as the index
df_sql.set_index('id', inplace=True)

### SQL data Ingestion ###

sql_ingest = sql_ingest()


### Vector dB Ingestion ###

input_data = df_merged.head(50).to_dict('records')

content_series = pd.Series(input_data)

processed_df = pd.DataFrame({'id' : [str(uuid.uuid4()) for _ in range(len(input_data))],
                            'content' : content_series})

processed_df["content"] = processed_df['content'].apply(lambda z: json.dumps(z))


emblist = []

def embedder(text):
    embedding = client.embeddings.create(input = text, model = 'text-embedding-ada-002')
    return embedding

for i in processed_df.index:
    emb = embedder(processed_df.loc[i]["content"]).data[0].embedding
    emblist.append(emb)

ids = processed_df.index.astype(str).tolist()
documents = processed_df["content"].tolist()

embeddings = emblist

print("Embeddings created .....")

print(documents)

old_count = chroma_col.count()
print("old_count :", old_count)
chroma_col.add(ids = ids, documents = documents, embeddings = embeddings)
new_count = chroma_col.count()
print("new_count :", new_count)
print(f"added {new_count-old_count} entries in collection - {col_name} Successfully \n ---- \n")
