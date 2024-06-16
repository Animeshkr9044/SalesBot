from handlers.vectordb_handler import store_embedding, query_embedding

class VectorService:
    def store_vector(self, vector, metadata):
        store_embedding(vector, metadata)

    def get_similar_vectors(self, vector, top_k=5):
        return query_embedding(vector, top_k)

vector_service = VectorService()
