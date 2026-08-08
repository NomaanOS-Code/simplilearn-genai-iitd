import math

print("="*65)
print("  NomaanOS - Pure Python Vector Cosine Similarity & RAG Engine")
print("="*65)

# Knowledge Base (Knowledge Chunks for RAG Retrieval)
documents = [
    "Private AI models run locally on constrained edge devices for maximum data sovereignty.",
    "Cybersecurity incident response requires log analysis and forensic threat intelligence.",
    "Generative AI and RAG architectures retrieve external context before generating responses.",
    "IIT Delhi IHFC drives robotics and autonomous cyber-physical system research."
]

# 1. Build Vocabulary & Term Frequency Vectorizer
def build_vocabulary(docs):
    vocab = set()
    for doc in docs:
        words = doc.lower().replace('.', '').replace(',', '').split()
        vocab.update(words)
    return sorted(list(vocab))

def text_to_vector(text, vocab):
    words = text.lower().replace('.', '').replace(',', '').split()
    return [words.count(word) for word in vocab]

# 2. Cosine Similarity Calculation Engine
def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    mag_v1 = math.sqrt(sum(a ** 2 for a in v1))
    mag_v2 = math.sqrt(sum(b ** 2 for b in v2))
    if mag_v1 == 0 or mag_v2 == 0:
        return 0.0
    return dot_product / (mag_v1 * mag_v2)

# Ingest Knowledge Base
vocab = build_vocabulary(documents)
doc_vectors = [text_to_vector(doc, vocab) for doc in documents]

# 3. RAG Query Retrieval Simulation
user_query = "How does local private AI maintain data sovereignty on edge?"
query_vec = text_to_vector(user_query, vocab)

print(f"\n[+] User Prompt / Query: '{user_query}'")
print(f"[+] Vector Space Dimension: {len(vocab)} unique tokens")

print("\n[+] RAG Context Retrieval & Similarity Scores:")
print("-" * 65)

retrieved_chunks = []
for idx, (doc, vec) in enumerate(zip(documents, doc_vectors), start=1):
    sim = cosine_similarity(query_vec, vec)
    retrieved_chunks.append((sim, doc))
    print(f" -> Chunk #{idx} | Similarity: {sim:.4f} | \"{doc[:50]}...\"")

# Sort Top Matching Context Block
retrieved_chunks.sort(key=lambda x: x[0], reverse=True)
best_chunk = retrieved_chunks[0]

print("-" * 65)
print(f"\n[🚀 Top RAG Context Selected]: Match Score = {best_chunk[0]:.4f}")
print(f" Prompt Context Injection Block: \"{best_chunk[1]}\"")
