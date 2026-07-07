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