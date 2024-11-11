from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key = openai_api_key)


def create_system_prompt(list_context):
    systemprompt = ''

    for context in list_context:
        if context != "":
            systemprompt += f"\n### Airlines Data ###\n"
            systemprompt += context + '\n'
    return systemprompt

def create_messages(input_query, prompt):
    system_message = [{'role' : 'assistant', 'content' : prompt}]
    query_message = [{'role':'user', 'content' : f"Analyzing the data to the best of your ability, {input_query}"}]
    return system_message + query_message


def get_llm_response_openai(query, instructions, list_context):

    sys_prompt = create_system_prompt(list_context)

    bot_prompt = f"""{instructions}

Below is the context for your reference.

Search Results:

{sys_prompt}
"""
    messages = create_messages(query, bot_prompt)
    with open("bot_mesage.txt","w") as promptfile:
        promptfile.write(str(bot_prompt))
    response = client.chat.completions.create(
        model='gpt-4o',
        messages=messages,
        temperature = 0.1,
        max_tokens=800
    )
    return response.choices[0].message.content

