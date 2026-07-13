def detect_agent_intent(query):
    normalized_query = query.lower().strip()

    action_keywords = [
        "액션 아이템",
        "할 일",
        "해야 할 일",
        "해야할 일",
        "업무",
        "체크리스트",
        "todo",
        "to-do",
    ]

    summary_keywords = [
        "요약",
        "정리",
        "간단히",
        "핵심",
    ]

    email_keywords = [
    "이메일",
    "메일",
    "답장",
    "답변 메일",
    "초안",
    "작성해줘",
    ]

    for keyword in action_keywords:
        if keyword in normalized_query:
            return "action_items"
    for keyword in email_keywords:
        if keyword in normalized_query:
            return "email_draft"

    for keyword in summary_keywords:
        if keyword in normalized_query:
            return "summary"

    return "qa"


def extract_action_items_from_text(text):
    lines = text.splitlines()
    action_items = []

    action_like_keywords = [
        "구현",
        "추가",
        "확인",
        "작성",
        "정리",
        "수정",
        "개선",
        "테스트",
        "표시",
        "업로드",
    ]

    for line in lines:
        clean_line = line.strip()

        if not clean_line:
            continue

        if clean_line.startswith("-"):
            action_items.append(clean_line.lstrip("-").strip())
            continue

        if clean_line[0:2].replace(".", "").isdigit():
            action_items.append(clean_line)
            continue

        for keyword in action_like_keywords:
            if keyword in clean_line:
                action_items.append(clean_line)
                break

    return action_items


def generate_action_items_answer(query, search_results):
    if not search_results:
        return "관련 문서를 찾지 못했습니다."

    all_action_items = []
    sources = []

    for item in search_results:
        document = item["document"]
        content = document["content"]

        action_items = extract_action_items_from_text(content)

        if action_items:
            source_text = f'{document["source"]}, chunk {document["chunk_id"]}'

            if source_text not in sources:
                sources.append(source_text)

            for action_item in action_items:
                all_action_items.append(action_item)

    if not all_action_items:
        return "검색된 문서에서 명확한 액션 아이템을 찾지 못했습니다."

    answer_lines = []
    answer_lines.append(f"질문 : {query}")
    answer_lines.append("")
    answer_lines.append("문서에서 추출한 업무 체크리스트는 다음과 같습니다.")
    answer_lines.append("")

    for index, action_item in enumerate(all_action_items, start=1):
        answer_lines.append(f"{index}. {action_item}")

    answer_lines.append("")
    answer_lines.append("출처:")
    for source in sources:
        answer_lines.append(f"- {source}")

    return "\n".join(answer_lines)

def generate_email_draft_answer(query, search_results):
    if not search_results:
        return "관련 문서를 찾지 못했습니다."

    top_result = search_results[0]
    document = top_result["document"]

    answer_lines = []
    answer_lines.append(f"질문 : {query}")
    answer_lines.append("")
    answer_lines.append("고객 문의 답변 이메일 초안:")
    answer_lines.append("")
    answer_lines.append("제목: 문의주신 내용에 대한 안내드립니다")
    answer_lines.append("")
    answer_lines.append("안녕하세요.")
    answer_lines.append("")
    answer_lines.append("문의해주셔서 감사합니다.")
    answer_lines.append("문의하신 내용과 관련하여 아래와 같이 안내드립니다.")
    answer_lines.append("")
    answer_lines.append(document["content"])
    answer_lines.append("")
    answer_lines.append("추가로 궁금하신 사항이 있으시면 언제든지 문의 부탁드립니다.")
    answer_lines.append("")
    answer_lines.append("감사합니다.")
    answer_lines.append("")
    answer_lines.append("출처:")
    answer_lines.append(f'- {document["source"]}, chunk {document["chunk_id"]}')

    return "\n".join(answer_lines)

def generate_summary_answer(query, search_results, all_chunks):
    if not search_results:
        return "관련 문서를 찾지 못했습니다."

    top_source = search_results[0]["document"]["source"]

    summary_contents = []
    sources = []

    for chunk in all_chunks:
        if chunk["source"] != top_source:
            continue

        content = chunk["content"].strip()

        # 제목처럼 너무 짧은 chunk는 제외
        if len(content) < 15:
            continue

        lines = [
            line.strip()
            for line in content.splitlines()
            if line.strip()
        ]

        if not lines:
            continue

        summary_contents.append(" ".join(lines[:3]))
        sources.append(f'{chunk["source"]}, chunk {chunk["chunk_id"]}')

    if not summary_contents:
        return "요약할 수 있는 문서 내용을 찾지 못했습니다."

    answer_lines = []
    answer_lines.append(f"질문 : {query}")
    answer_lines.append("")
    answer_lines.append(f"{top_source} 문서 핵심 요약:")
    answer_lines.append("")

    for index, content in enumerate(summary_contents, start=1):
        answer_lines.append(f"{index}. {content}")

    answer_lines.append("")
    answer_lines.append("출처:")
    for source in sources:
        answer_lines.append(f"- {source}")

    return "\n".join(answer_lines)


def run_agent_action(query, search_results, all_chunks):
    intent = detect_agent_intent(query)

    if intent == "action_items":
        return generate_action_items_answer(query, search_results)
    
    if intent == "email_draft":
        return generate_email_draft_answer(query, search_results)
    
    if intent == "summary":
        return generate_summary_answer(query, search_results, all_chunks)

    return None