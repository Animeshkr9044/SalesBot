import pinecone
from config import PINECONE_API_KEY

pinecone.init(api_key=PINECONE_API_KEY, environment='us-west1-gcp')
index = pinecone.Index('salesbot-index')

def store_embedding(vector, metadata):
    index.upsert([(str(metadata['id']), vector)])

def query_embedding(vector, top_k=5):
    result = index.query(vector, top_k=top_k)
    return result['matches']
