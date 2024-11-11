import json
import sqlite3
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key = openai_api_key)



with open('schema.txt', 'r') as file:
    schema = file.read()



bot_instructions = '''You are an AI Assistant assistant that helps in answering queries regarding Airlines.\n
Your main task is to generate SQL queries for sqlite database given input queries from user.
Also you have to classify the input query into Airlines related or others.
Also you have to extract which Airline is mentioned in the query.
One important information while creating SQL queries is that below are the some of the Airlines.
1. Air Canada
2) Air Canada
3) Air France
4) Alaska Airlines
5) Allegiant Air
6) American Airline
7 )British Airways
8) ------------
9) -------------, etc..

So create the queries as per the input query question.
One important instruction for you is dont try to generate sql queries from your own entirely different from below examples. Try to closely follow the where clause shown in each of the query, if input user query matches any one of the Query below, then generate the sql_query as shown in output query.

Dont answer any user query which is not related to Airlines. Simply tag class as "out_us" in output.
Some of the few shot examples for generating queries for your understanding given below : \n
1. Query: Which airline has the most flights listed ? output query: {"class":"flight_count","sql_query":"WITH MaxFlightCount AS ( SELECT MAX(flight_count) AS max_count FROM ( SELECT COUNT(*) AS flight_count FROM Airlines_data GROUP BY airline_name )) SELECT airline_name, COUNT(*) AS flight_count FROM Airlines_data GROUP BY airline_name HAVING flight_count = (SELECT max_count FROM MaxFlightCount);"} \n
2. Query: Which airline has the listed less number of flights ? output query: {"class":"flight_count","sql_query":"WITH MinFlightCount AS (SELECT MIN(flight_count) AS min_count FROM (SELECT COUNT(*) AS flight_count FROM Airlines_data GROUP BY airline_name ) ) SELECT airline_name, COUNT(*) AS flight_count FROM Airlines_data GROUP BY airline_name HAVING flight_count = (SELECT min_count FROM MinFlightCount);"} \n
3. Query: How many flights listed for American Airlines ? output query: {"class":"flight_count","sql_query":"SELECT COUNT(*) AS flight_count FROM Airlines_data WHERE airline_name = 'American Airlines';"} \n
4. Query: How many flights listed for Alaskan Airlines ? output query: {"class":"flight_count","sql_query":"SELECT COUNT(*) AS flight_count FROM Airlines_data WHERE airline_name = 'Alaskan Airlines';"} \n
5. Query: Can you provide a list of top-rated universities and colleges? output query: {"class": "others", "sql_query":"No SQL"} \n
6. Query: What are some must-visit tourist attractions and scenic spots ? output query: {"class":"others", "sql_query": "No SQL"} \n
7. Query: Who is Prime Minister of USA? output query: {"class":"others","sql_query":"No SQL"} \n
8. Query: Tell me about rental properties with high social and transport access available in 7 days in Manchester?? output query: {"class":"out_us", "sql_query": "No SQL"} \n
9. Query: What is the current vacancy trend in Tokyo vis a vis over last year? output query: {"class":"out_us", "sql_query": "No SQL"} \n
0. Query: What is the current trend w.r.t. to cap rate in Lucknow? output query: {"class":"out_us", "sql_query":"No SQL"} \n

Please return the output in proper json format as shown in above few shot examples, dont miss any closing brackets in the repsonse.'''




def create_context(question, schema):

    context = "Write SQL Query for SQLite Database, the schema for the tables are as follows:"+ schema + "\n. Below is the query asked by user. Query:"+ question
    # Return the context
    return "".join(context)


def generate_query_explain(context,bot_instructions, question):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role":"system","content": bot_instructions},
                    {"role":"user","content":context}],
        temperature = 0.1,
        max_tokens=800
    )
    resp = response.choices[0].message.content
    resp = json.loads(resp)

    cls = resp['class']

    if cls == "flight_count":
        gen_query = resp["sql_query"]
        conn = sqlite3.connect('Airlines.db')
        df = pd.read_sql_query(gen_query, conn)
        rec = df.to_dict('records')
        return rec
    

def generate_bot_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role":"system","content": 'You are an AI Assistant'},
                    {"role":"user","content":prompt}],
        temperature = 0.1,
        max_tokens=800
    )
    return response.choices[0].message.content

def answer_question(ques):
    context = create_context(ques, schema)
    resp_sql = generate_query_explain(context, bot_instructions, ques)
    prompt = "for the query: " + ques +" and here is the below response from the database. Frame your response by analyzing the flight count from below response taken from the database \n " + str(resp_sql)
    bot_response =  generate_bot_response(prompt)

    return bot_response










        




#resp = response["choices"][0]["message"]["content"]
# resp = json.loads(resp)
# cls = resp["class"]
# if cls == "others":
# prompt="Category of conversation is Others"
# =
# items generate_response(prompt) city="None"
# return items,cls, city
# elif cls =="out_us":
# prompt='''Greet the user stating Thanks for asking your question, but unfortunately
# we dont support regions outside US. Please feel free to ask queries related to properties in US.' items generate_out_response(prompt)
# city="None"
# return items,cls,city


