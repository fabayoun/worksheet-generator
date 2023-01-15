from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_cosine_similarity(answer: str, context: str) -> bool:
    sentences = [answer, context]
    model = SentenceTransformer('bert-base-nli-mean-tokens')
    sentence_embeddings = model.encode(sentences)
    return round(cosine_similarity([sentence_embeddings[0], sentence_embeddings[1]])[0][1], 3)
