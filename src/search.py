#문장/문서를 숫자 백터로 바꾸는 도구
from sklearn.feature_extraction.text import TfidfVectorizer
#두 숫자 백터가 얼마나 비슷한지 계산하는 도구
from sklearn.metrics.pairwise import cosine_similarity


def search_documents(query, documents, top_k=3, min_score = 0.1):
    #text에 doc내용만 저장
    texts = [doc["content"] for doc in documents]

    #문서에서 중요한 단어/글자 조각에 높은 점수주고 흔한 조각에는 낮은 점수를 줌
    #글자 단위로  쪼갬(한국어 영어는 공백으로 진행할 예정)
    #2글자 3글자 묶어서 봄
    vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 3))
    #chunk를 숫자로 바꿈
    document_vectors = vectorizer.fit_transform(texts)

    #질문을 숫자로 바굼
    query_vector = vectorizer.transform([query])
    #질문벡터, 문서벡터 유사도 검사 cosin_similarity 는 2차원 배열이로 나와서 [0] 붙임
    similarities = cosine_similarity(query_vector, document_vectors)[0]
    #가장 관련 높은 chunk index부터 정렬
    ranked_indices = similarities.argsort()[::-1]

    results = []
#여기까지----------------------------
    for rank, index in enumerate(ranked_indices[:top_k],start=1):
        score = similarities[index]

        if score > min_score:
            results.append({
                "rank" : rank,
                "document": documents[index],
                "score": score
            })

    return results