from sentence_transformers import SentenceTransformer, util

# Load the model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def get_similarity_score(resume_text, jd_text):
    embeddings = model.encode([resume_text, jd_text], convert_to_tensor=True)
    similarity = util.cos_sim(embeddings[0], embeddings[1])
    return round(similarity.item() * 100, 2)
