import streamlit as st
import openai
from Query_Orchestration import query_orchestration

st.title("Airlines AI Assistant")
st.write("Enter a query and get a response below:")

# Text input from the user
user_input = st.text_area("Enter your query here:", "")



if st.button("Get Response"):
    if user_input.strip() == "":
        st.warning("Please enter a query.")
    else:
        # Get and display the response
        response_text = query_orchestration(user_input)
        st.text_area("Response:", response_text, height=400)
