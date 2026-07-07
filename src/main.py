from pathlib import Path
from search import search_documents
from generator import generate_answer

DOCS_DIR = Path("sample_docs")


def load_documents():
    documents = []

    for file_path in DOCS_DIR.glob("*.txt"):
        text = file_path.read_text(encoding="utf-8")

        documents.append({
            "source": file_path.name,
            "content": text
        })

    return documents


def split_documents_into_chunks(documents):
    chunks = []

    for doc in documents:
        paragraphs = doc["content"].split("\n\n")

        for index, paragraph in enumerate(paragraphs):
            clean_text = paragraph.strip()

            if clean_text:
                chunks.append({
                    "source": doc["source"],
                    "chunk_id": index + 1,
                    "content": clean_text
                })

    return chunks


def main():
    documents = load_documents()
    chunks = split_documents_into_chunks(documents)

    print("문서 로드 완료")
    print(f"총 문서 수: {len(documents)}개")
    print(f"총 chunk 수: {len(chunks)}개")

    print("-" * 40)

    query = input("질문을 입력하세요: ")

    results = search_documents(query, chunks, top_k=3)

    print("-" * 40)
    print("사용자 질문:", query)

    if not results:
        print("관련 있는 문서를 찾지 못했습니다.")
    else:
        print("관련 문서 검색 결과")

        for rank, item in enumerate(results, start=1):
            document = item["document"]
            score = item["score"]

            print("-" * 40)
            print(f"{rank}위")
            print("문서:", document["source"])
            print("chunk 번호:", document["chunk_id"])
            print("내용:", document["content"])
            print("유사도 점수:", score)
        answer = generate_answer(query, results)
        print("-" *40)
        print("생성된 답변")
        print(answer)
if __name__ == "__main__":
    main()