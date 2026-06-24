text = """2026년 6월 23일 회의록

주제: AI 문서 검색 서비스 개발 방향

결정사항:
1. 초기 버전은 txt 문서 검색부터 구현한다.
2. 이후 PDF 업로드 기능을 추가한다.

액션 아이템:
- 광수: Python 기반 문서 검색기 구현
- 팀원 A: 샘플 문서 정리
"""


paragraphs = text.split("\n\n")

chunks =[]

for index, paragraph in enumerate(paragraphs):
    clean_paragraph = paragraph.strip()
    
    chunks.append({
        "chunk_id" : index + 1,
        "source" : "meeting_note.txt",
        "content" : clean_paragraph
    })
print("총 문단수 : ", len(paragraphs))
print("총 청크 수 : ",len(chunks))

for chunk in chunks:
    print("-"*40)
    print("chunk 번호 :", chunk["chunk_id"])
    print("출처 :",chunk["source"])
    print("내용 :",chunk["content"])