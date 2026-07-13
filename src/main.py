from pathlib import Path
from search import search_documents
from generator import generate_answer, is_greeting, generate_greeting_answer


#문서가 있을 위치 정하기  DOCS_DIR = Path("sample_docs")
DOCS_DIR = Path("sample_docs")

#sample_docs 폴더안의 txt 파일을 모두 읽는 함수
def load_documents():
    documents = []
                    #DOCS_DIR = sample_docs 안에 .txt로 끝나는 파일들을 전부 찾기
    for file_path in DOCS_DIR.glob("*.txt"):
                                    #utf-8방식으로 읽어 한글 깨짐 방지
        text = file_path.read_text(encoding="utf-8")
        #딕셔너리로  묶어 리스트에 추가
        documents.append({
            "source": file_path.name, #company_policy.txt
            "content": text
        })

    return documents


def split_documents_into_chunks(documents):
    chunks = []
                #documents의 리스트 내용을 하나 씩 꺼냄
    for doc in documents:
                #문서 내용을 빈 줄 기준으로 나눈다
        paragraphs = doc["content"].split("\n\n")
        #enumerate는 리스트에서 값과 순서 같이 꺼냄
        for index, paragraph in enumerate(paragraphs):
            #공백 제거 
            clean_text = paragraph.strip()

            if clean_text: #빈 문단 제외 공백은 False
                chunks.append({
                    "source": doc["source"],
                    "chunk_id": index + 1,
                    "content": clean_text
                })

    return chunks


def main():
    #문서파일 읽기
    documents = load_documents()
    #읽은 문선 문단 단위로 chunk로 나눔
    chunks = split_documents_into_chunks(documents)

    print("문서 로드 완료")
    print(f"총 문서 수: {len(documents)}개")
    print(f"총 chunk 수: {len(chunks)}개")

    print("-" * 40)

    query = input("질문을 입력하세요: ")

    if is_greeting(query):
        print("-" * 40)
        print("생성된 답변")
        print(generate_greeting_answer())
        return
    #가장 관련있는 3개 찾기
    results = search_documents(query, chunks, top_k=3, min_score=0.1)

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