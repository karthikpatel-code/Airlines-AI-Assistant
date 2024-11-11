import os
import chromadb
from openai import OpenAI
from get_llm_respponse import get_llm_response_openai
from dotenv import load_dotenv
chroma_root = r"chromadb"
chroma_client = chromadb.PersistentClient(path = chroma_root)
col_name = "Airlines_data"

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')


client = OpenAI(api_key = openai_api_key)


def embedder(text):
    embedding = client.embeddings.create(input = text, model = 'text-embedding-ada-002').data[0].embedding
    return embedding




def chunk_collation(query):
    query_emb = embedder(query)
    n=50
    chroma_col = chroma_client.get_collection(name = col_name)
    result = chroma_col.query(query_embeddings=query_emb, include = ['documents','distances'], n_results=n)

    return { "generated_context" : {
        "Composed_chunks" : result['documents'][0]
    }

    }