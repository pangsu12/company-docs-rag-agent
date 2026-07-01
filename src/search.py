from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def search_documents(query, documents, top_k=3):
    texts = [doc["content"] for doc in documents]

    vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 3))

    document_vectors = vectorizer.fit_transform(texts)
    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(query_vector, document_vectors)[0]

    ranked_indices = similarities.argsort()[::-1]

    results = []

    for index in ranked_indices[:top_k]:
        score = similarities[index]

        if score > 0:
            results.append({
                "document": documents[index],
                "score": score
            })

    return results