from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


documents = [
    {
        "source": "company_policy.txt",
        "content": "연차 사용은 최소 3일 전에 팀장에게 신청해야 한다."
    },
    {
        "source": "meeting_note.txt",
        "content": "광수는 Python 기반 문서 검색기 구현을 맡았다."
    },
    {
        "source": "faq.txt",
        "content": "이 서비스는 회사 문서를 기반으로 답변하는 AI Agent 서비스입니다."
    },
    {
        "source": "email_sample.txt",
        "content": "고객 문의에 대한 답변 이메일 초안을 작성해야 한다."
    }
]

def search_documents(qurey, documents):
    texts = [doc["content"] for doc in documents]

    vectorizer =TfidfVectorizer(analyzer="char", ngram_range=(2, 3))
    document_vectors = vectorizer.fit_transform(texts)
    query_vector = vectorizer.transform([query])
    similarities =cosine_similarity(query_vector, document_vectors)

    best_index = similarities.argmax()
    best_document = documents[best_index]
    best_score = similarities[0][best_index]
    if best_score == 0:
     return None, best_score

    return best_document, best_score    
query = input("질문을 입력하세요: ")

best_document, best_score = search_documents(query, documents)

print("-" * 40)
print("사용자 질문:", query)

if best_document is None:
    print("관련 있는 문서를 찾지 못했습니다.")
    print("유사도 점수:", best_score)
else:
    print("가장 관련 있는 문서:", best_document["source"])
    print("문서 내용:", best_document["content"])
    print("유사도 점수:", best_score)