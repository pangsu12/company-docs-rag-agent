import os

from dotenv import load_dotenv
from openai import OpenAI, RateLimitError, APIError


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI() if api_key else None


def is_greeting(query):
    greetings = ["안녕", "안녕하세요", "하이", "hello", "hi"]

    normalized_query = query.lower().strip()

    for greeting in greetings:
        if greeting in normalized_query:
            return True

    return False


def generate_greeting_answer():
    return "안녕하세요. 회사 문서에 대해 궁금한 내용을 질문해주세요."


def build_context(search_results):
    context_parts = []

    for index, item in enumerate(search_results, start=1):
        document = item["document"]

        context_parts.append(
            f"""
[문서 {index}]
출처: {document["source"]}, chunk {document["chunk_id"]}
내용:
{document["content"]}
"""
        )

    return "\n".join(context_parts)


def generate_fallback_answer(query, search_results):
    if not search_results:
        return "관련 문서를 찾지 못했습니다."

    top_result = search_results[0]
    document = top_result["document"]
    search_file_count = len(search_results)

    answer = f"""
질문 : {query}

총 {search_file_count}개의 문서를 찾았습니다.

관련 문서에 따르면:
{document["content"]}

출처 : {document["source"]}, chunk {document["chunk_id"]}
"""

    return answer


def generate_answer(query, search_results):
    if not search_results:
        return "관련 문서를 찾지 못했습니다."

    context = build_context(search_results)

    prompt = f"""
아래 회사 문서 내용을 참고해서 사용자의 질문에 답변하세요.

규칙:
1. 반드시 제공된 문서 내용만 근거로 답변하세요.
2. 문서에 없는 내용은 추측하지 말고 "제공된 문서에서는 확인할 수 없습니다."라고 답변하세요.
3. 답변은 한국어로 작성하세요.
4. 마지막에 출처를 표시하세요.
5. 너무 길게 쓰지 말고 핵심만 정리하세요.

회사 문서:
{context}

사용자 질문:
{query}
"""

    if client is None:
        print("OpenAI API 키가 없어 fallback 답변을 사용합니다.")
        return generate_fallback_answer(query, search_results)

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt,
            temperature=0.2,
            max_output_tokens=500,
        )

        return response.output_text

    except RateLimitError:
        print("OpenAI API 사용량/결제 제한으로 fallback 답변을 사용합니다.")
        return generate_fallback_answer(query, search_results)

    except APIError as error:
        print(f"OpenAI API 오류로 fallback 답변을 사용합니다: {error}")
        return generate_fallback_answer(query, search_results)

    except Exception as error:
        print(f"예상하지 못한 오류로 fallback 답변을 사용합니다: {error}")
        return generate_fallback_answer(query, search_results)