def is_greeting(query):
    grettings = ["안녕","안녕하세요","하이","hello","hi"]

    normalized_query = query.lower().strip()

    for greeting in grettings:
        if greeting in normalized_query:
            return True
    return False

def generate_greeting_answer():
    return "안녕하세요. 회사 문서에 대해 궁금한 내용을 질문해주세요."


def generate_answer(query, search_results):
    if not search_results:
        return "관련 문서를 찾지 못했습니다."
    

    top_result = search_results[0]
    document = top_result["document"]

    answer = f"""
질문 : {query}

관련 문서에 따르면:
{document["content"]}

출처 : {document["source"]}, chunk{document["chunk_id"]}
"""
    
    return answer