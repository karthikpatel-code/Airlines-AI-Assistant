# Airlines-AI-Assistant
# Overview:
The **Airlines Data Assistant** is an intelligent conversational AI solution designed to answer user queries about airline-related data. It combines a **Retrieval-Augmented Generation (RAG)** pipeline and a **SQL-based** pipeline, powered by **ChromaDB embeddings** and **SQLite3**, respectively. The assistant is designed with deflection logic that **intelligently routes** queries to either the **SQL pipeline** or the **RAG pipeline** based on a few-shot learning approach. This ensures that user queries are handled efficiently, with the right pipeline being used based on the nature of the query, allowing the assistant to provide precise and data-driven responses.

## Key Features:

* **OpenAI LLM Endpoints**: The system leverages OpenAI's API endpoints to generate responses for both structured and unstructured queries. These endpoints process natural language queries and generate meaningful,   relevant answers.
* **Deflection Logic**: The system intelligently routes queries to the appropriate pipeline based on predefined rules and a few-shot learning model. For example, queries related to structured data (e.g., flight counts, airline bookings) are directed to the SQL pipeline, while unstructured queries (e.g., summaries, insights, comparisons) are routed to the RAG pipeline.
* **Context-Aware Responses**: Using ChromaDB embeddings, the assistant retrieves context-specific data and uses it in combination with both the SQL and RAG pipelines to provide the most accurate and relevant responses.
* **Hybrid RAG + SQL Pipeline**: A robust hybrid architecture that combines the strengths of both RAG (contextual retrieval and generation) and SQL (precise data querying) to handle a wide range of queries.
Natural Language Interaction: The assistant provides natural, human-like interactions, responding to user queries about flight details, bookings, destinations, airline rankings, and more.

## Architecture Diagram

![Airlines AI Assist](https://github.com/user-attachments/assets/8478bd2e-ff87-4888-853e-ef3ed858aec6)



## Project Prerequisites
To run this project, Install Python (version 3.11 recommended) and use pip to install the required packages

## Installation
1. Clone the Repository
   ```bash
   git clone https://github.com/karthikpatel-code/Airlines-AI-Assistant.git
   
2. Install the Dependencies
      ```bash
   pip install -r requirements.txt

3. Run the System:
      ```bash
   streamlit run UI.py
   
## How It Works:
1. **User Interaction**:
   * The user asks a query such as "How many flights does American Airlines have?" or "What is the most frequent destination for Airline X?"
  
2. **Deflection Logic**:
   * The deflection logic is invoked to decide which pipeline (SQL or RAG) should handle the query. This is based on a few-shot learning model that classifies whether the query requires structured data or more context-based generation.
     
3. **Pipeline Execution**:
   * SQL Pipeline: For structured data, the assistant routes the query to the SQL pipeline, where it executes SQL queries against an SQLite3 database. The assistant uses OpenAI's endpoints for natural language processing to translate user queries into SQL queries.
   * RAG Pipeline: For unstructured queries, the assistant utilizes the RAG pipeline with ChromaDB embeddings to retrieve context from past interactions or stored data. The assistant then uses OpenAI LLM endpoints to generate an insightful response based on the retrieved context.
     
4. **OpenAI LLM API Calls**:
    * Both pipelines leverage OpenAI’s API for natural language processing and response generation:
        * For SQL-related queries, OpenAI LLM endpoints assist in translating the user’s natural language input into the corresponding SQL query.
        * For RAG-based queries, the OpenAI API generates insightful answers based on context retrieved from ChromaDB embeddings.

## Response Generation:

* The SQL pipeline returns precise, factual data (e.g., "American Airlines operates 120 flights").
* The RAG pipeline generates insightful, context-based responses, such as summaries or comparisons.
* Both pipelines feed into the final response generator, ensuring the user receives a complete and informative answer.
  
## Final Answer:

Based on the data retrieved from either pipeline, the assistant constructs and delivers a comprehensive response to the user.


## Technologies Used:
* **Python**: Core language used for development.
* **OpenAI GPT-3.5/4**: Used for natural language processing, understanding, and response generation.
* **ChromaDB**: A vector database that stores embeddings for semantic search and retrieval.
* **SQLite3**: Used for storing structured airline data, such as flight counts, bookings, and destinations.
* **Streamlit**: Framework for creating a user-friendly interface.
* **Retrieval-Augmented Generation (RAG)**: Combines knowledge retrieval and generation to answer complex queries.
* **Natural Language to SQL (NL_to_SQL)**: Converts user queries into SQL queries for precise database retrieval.
* **Deflection Logic**: Routes queries to the appropriate pipeline (SQL or RAG) based on the nature of the query using a few-shot learning approach.

## Deflection Logic Workflow:
The deflection logic uses a simple decision model to route queries between the SQL and RAG pipelines:

1. **Query Classification**:
   * The query is first classified to determine if it requires structured data (SQL) or context-based response (RAG).
   * **SQL-related Queries**: These include requests for data like flight counts, airline bookings, or destinations. Example queries:
      * "How many flights does American Airlines have?"
      * "Which airline operates the most flights?"
      * "What is the number of bookings for Delta Airlines?"
   * **RAG-related Queries**: These involve contextual insights, comparisons, or trend analysis. Example queries:
      * "What are the most frequent destinations for each airline?"
2. **Pipeline Routing**:
    * SQL Pipeline: For structured queries, the system constructs and executes SQL queries to fetch data from the SQLite3 database.
    * RAG Pipeline: For complex, unstructured queries, the system retrieves contextually relevant information from the ChromaDB embeddings.
3. **Query Handling**:
    Based on the classification, the appropriate pipeline (SQL or RAG) is invoked to fetch the relevant information.
4. **Response Construction**:
    * **SQL Pipeline Responses**: These are precise, data-driven answers like "American Airlines has 120 flights listed."
    * **RAG Pipeline Responses**: These are generated insights, summaries, and comparisons based on the embeddings.

## Test Cases Verified

1. Which airline has the most flights listed ?
2. Which airline has the least flights listed ?
3. What is the flight count of Delta Airlines ?
4. Month with the highest number of bookings ?
5. Patterns in booking cancellations, focusing on specific days or airlines with high cancellation rates
6. Analyze seat occupancy to find the most and least popular flights.
  
## Sample Outputs :
  
![image](https://github.com/user-attachments/assets/a1fbb234-1bc8-4c31-ba49-ad82832beb0e)

![image](https://github.com/user-attachments/assets/6cfad83b-eacf-4058-b2cb-5fd0149ea4dd)

![image](https://github.com/user-attachments/assets/fa648330-86a8-4922-ad55-d473e2f1947e)

![image](https://github.com/user-attachments/assets/fbb54854-7194-45c8-8b2f-1ffbb332a0af)

![image](https://github.com/user-attachments/assets/f73a2e44-d050-425a-bb6d-a0a7ce926740)

## Expected Outcomes:
* **Accurate Responses**: By leveraging OpenAI API endpoints for both SQL query generation and context-based answer generation, the system ensures that user queries receive precise, relevant responses.
* **Efficient Query Handling**: The deflection logic optimizes query processing by directing them to the correct pipeline, ensuring that responses are generated quickly and accurately.
* **User-Friendly Interaction**: The system provides a smooth and natural conversational experience for the user, powered by OpenAI LLM endpoints and data from SQLite3 and ChromaDB.
The integration of OpenAI's LLM endpoints enables the Airlines Data Assistant to effectively handle a wide range of queries, providing users with highly informative and context-aware responses.

## Future Enhancements

Given that your current solution was developed with a minimal dataset, here are some specific ways to optimize and enhance it with larger datasets:
1. **Scale Data Sources**: Integrate additional airline and travel-related datasets, such as airport information, weather data, and customer reviews. This will expand your solution’s ability to answer more detailed and varied questions.
2. **Enhanced Indexing and Query Efficiency**: Optimize indexing methods within ChromaDB (or other databases used), and consider precomputing embeddings for frequent queries to improve retrieval times as the data volume grows.
3. **Model Fine-tuning and Customization**: With more data, fine-tune the LLM model on airline-specific language and concepts, improving its relevance and accuracy when responding to queries related to the airline industry.
4. **Scalability Testing and Load Balancing**: As you scale, simulate a high load environment to test the system's performance. Introduce load balancing and caching mechanisms to manage a larger dataset efficiently.
5. **Storage Optimization**: For larger datasets, optimize storage strategies, like using cloud-based scalable storage solutions, to maintain data availability without compromising performance.
6. **Real-Time Data Integration**:
    * **Enhancement**: Incorporate real-time airline data, such as live flight statuses, delays, and weather conditions, to offer more up-to-date responses.
    * **Benefit**: Provides users with dynamic and actionable insights, especially valuable for time-sensitive queries.

## Contributor

Karthik Patelkana
