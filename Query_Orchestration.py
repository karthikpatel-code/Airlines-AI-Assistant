import chromadb
from openai import OpenAI
from get_llm_respponse import get_llm_response_openai
from chunk_collation import chunk_collation
from deflection_logic import deflect_query
from NLP_to_sql import answer_question



with open("prompt.txt", "r") as file:
    bot_instructions = file.read()

def query_orchestration(user_query):
    deflection_response = deflect_query(user_query)
    if deflection_response['query_type'] == "RAG":
        print("In RAG Pipeline.....")
        chunk_collation_result = chunk_collation(user_query)
        listcontext = chunk_collation_result["generated_context"]["Composed_chunks"]
        response = get_llm_response_openai(user_query, bot_instructions, listcontext)
        return response
    else:
        print("In NLP to SQL Pipeline.....")
        sql_pipeline_resp = answer_question(user_query)
        return sql_pipeline_resp




# uq = "Analyzing the data to the best of your ability determine patterns in booking cancellations, focusing on specific days or airlines with high cancellation rates."
# uq = "Analyzing the data to the best of your ability determine the Month in 2023 with the highest number of bookings."
# uq = "Which airline has the most flights listed ?"

# print(query_orchestration(uq))


