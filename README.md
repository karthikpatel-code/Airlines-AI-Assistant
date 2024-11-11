# Airlines-AI-Assistant
# Overview:
The Airlines Data Assistant is an intelligent conversational AI solution designed to answer user queries about airline-related data. It combines a Retrieval-Augmented Generation (RAG) pipeline and a SQL-based pipeline, powered by ChromaDB embeddings and SQLite3, respectively. The assistant is designed with deflection logic that intelligently routes queries to either the SQL pipeline or the RAG pipeline based on a few-shot learning approach. This ensures that user queries are handled efficiently, with the right pipeline being used based on the nature of the query, allowing the assistant to provide precise and data-driven responses.

# Key Features:

OpenAI LLM Endpoints: The system leverages OpenAI's API endpoints to generate responses for both structured and unstructured queries. These endpoints process natural language queries and generate meaningful,   relevant answers.
Deflection Logic: The system intelligently routes queries to the appropriate pipeline based on predefined rules and a few-shot learning model. For example, queries related to structured data (e.g., flight counts, airline bookings) are directed to the SQL pipeline, while unstructured queries (e.g., summaries, insights, comparisons) are routed to the RAG pipeline.
Context-Aware Responses: Using ChromaDB embeddings, the assistant retrieves context-specific data and uses it in combination with both the SQL and RAG pipelines to provide the most accurate and relevant responses.
Hybrid RAG + SQL Pipeline: A robust hybrid architecture that combines the strengths of both RAG (contextual retrieval and generation) and SQL (precise data querying) to handle a wide range of queries.
Natural Language Interaction: The assistant provides natural, human-like interactions, responding to user queries about flight details, bookings, destinations, airline rankings, and more.


# How It Works:
User Interaction:

The user asks a query such as "How many flights does American Airlines have?" or "What is the most frequent destination for Airline X?"
Deflection Logic:

The deflection logic is invoked to decide which pipeline (SQL or RAG) should handle the query. This is based on a few-shot learning model that classifies whether the query requires structured data or more context-based generation.
SQL Pipeline: If the query involves precise data points like flight counts, bookings, or other structured information, the query is routed to the SQL pipeline.
RAG Pipeline: If the query requires a contextual, detailed response or summary, such as trends or comparisons, the query is routed to the RAG pipeline.
SQL Pipeline Query Execution:

For queries routed to the SQL pipeline, the system generates SQL queries to fetch relevant data from the SQLite3 database. This allows for exact retrieval of structured data.
RAG Pipeline Query Execution:

For queries routed to the RAG pipeline, the system uses ChromaDB embeddings to retrieve contextually relevant data. This enables the assistant to provide high-level insights, summaries, and comparisons based on the stored data.
Response Generation:

The SQL pipeline returns precise, factual data (e.g., "American Airlines operates 120 flights").
The RAG pipeline generates insightful, context-based responses, such as summaries or comparisons (e.g., "American Airlines has the most flights listed among all airlines, followed by Delta Airlines").
Both pipelines feed into the final response generator, ensuring the user receives a complete and informative answer.
Final Answer:

Based on the data retrieved from either pipeline, the assistant constructs and delivers a comprehensive response to the user.


# Technologies Used:
Python: Core language used for development.
OpenAI GPT-3.5/4: Used for natural language processing, understanding, and response generation.
ChromaDB: A vector database that stores embeddings for semantic search and retrieval.
SQLite3: Used for storing structured airline data, such as flight counts, bookings, and destinations.
Streamlit: Framework for creating a user-friendly interface.
Retrieval-Augmented Generation (RAG): Combines knowledge retrieval and generation to answer complex queries.
Natural Language to SQL (NL_to_SQL): Converts user queries into SQL queries for precise database retrieval.
Deflection Logic: Routes queries to the appropriate pipeline (SQL or RAG) based on the nature of the query using a few-shot learning approach.

# Deflection Logic Workflow:
The deflection logic uses a simple decision model to route queries between the SQL and RAG pipelines:

Query Classification:

The query is first classified to determine if it requires structured data (SQL) or context-based response (RAG).

SQL-related Queries: These include requests for data like flight counts, airline bookings, or destinations. Example queries:

"How many flights does American Airlines have?"
"What is the number of bookings for Delta Airlines?"
RAG-related Queries: These involve contextual insights, comparisons, or trend analysis. Example queries:

"Which airline operates the most flights?"
"What are the most frequent destinations for each airline?"
Pipeline Routing:

SQL Pipeline: For structured queries, the system constructs and executes SQL queries to fetch data from the SQLite3 database.
RAG Pipeline: For complex, unstructured queries, the system retrieves contextually relevant information from the ChromaDB embeddings.
Query Handling:

Based on the classification, the appropriate pipeline (SQL or RAG) is invoked to fetch the relevant information.
Response Construction:

SQL Pipeline Responses: These are precise, data-driven answers like "American Airlines has 120 flights listed."
RAG Pipeline Responses: These are generated insights, summaries, and comparisons based on the embeddings.

# Expected Outcomes:
Accurate Responses: By leveraging OpenAI API endpoints for both SQL query generation and context-based answer generation, the system ensures that user queries receive precise, relevant responses.
Efficient Query Handling: The deflection logic optimizes query processing by directing them to the correct pipeline, ensuring that responses are generated quickly and accurately.
User-Friendly Interaction: The system provides a smooth and natural conversational experience for the user, powered by OpenAI LLM endpoints and data from SQLite3 and ChromaDB.
The integration of OpenAI's LLM endpoints enables the Airlines Data Assistant to effectively handle a wide range of queries, providing users with highly informative and context-aware responses.
