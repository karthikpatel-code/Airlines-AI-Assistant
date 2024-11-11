from openai import OpenAI
from dotenv import load_dotenv
import os
import json
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key = openai_api_key)




def deflect_query(question):
    trifurcation_prompt = f"""You are an AI assistant that helps in identifying the type of query asked by the user. Your task is to identify whether the query is related to SQL Pipeline or related to RAG Pipeline. Return json output with key as query type and its value as SQL or RAG.

One important instruction for you is that only if the user query is related to flight count of Airlines determine its query_type as SQL. Determine the query_type as "RAG" for all other user queries.

Some of the few shot examples for your your understanding given below :
Query: Which airline has the most flights listed ? output json: {{"query_type":"SQL"}} \n
Query: Which airline has the least flights listed? output json: {{"query_type":"SQL"}} \n
Query: How many flights listed for Alaskan Airlines ? output json: {{"query_type":"SQL"}} \n
Query: How many flights listed for Lufthansa ? output json: {{"query_type":"SQL"}} \n
Query: Number of bookings for American Airlines in the June 2023 ? output json: {{"query_type":"RAG"}} \n
Query: Number of bookings for Emirates Airlines in the July 2023 ? output json: {{"query_type":"RAG"}} \n
Query: Analyze seat occupancy to find the most and least popular flights ? output json: {{"query_type":"RAG"}} \n
Query: Patterns in booking cancellations, focusing on specific days or airlines with high cancellation rates? output json: {{"query_type":"RAG"}} \n
Query: Average flight delay per airline. ? output json: {{"query_type":"RAG"}} \n

Now Identify the query type of the below input query. Query: {question}
Please return the output in proper json format as shown in above few shot examples, dont miss any closing brackets in the repsonse."""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"system","content": trifurcation_prompt},
                    {"role":"user","content":question}],
        temperature = 0.1,
        max_tokens=800
    )
    resp = response.choices[0].message.content
    return json.loads(resp)



