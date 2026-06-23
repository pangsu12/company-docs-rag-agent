name = "광수"
goal = "AI 엔지니어"

print("이름 : " ,name)
print("목표 : ", goal)

print("-" * 40)

document = [
    "company_policy.txt",
    "meeting_noet.txt",
    "fag.txt",
    "ai_practice"
]

print("문서목록 : " , document)
print("첫 번째 뮨서 : ",document[0])

print("두 번째 뮨서 : ",document[1])

print("세 번째 뮨서 : ",document[2])
print("네 번째 목록 : ", document[3])
print("총 문서 수 : ", len(document))

print("-" * 40)

document = {
    "source" : "company_policy.txt",
    "content": "연차 사용은 최소 3일 전에 팀장에게 신청해야 한다.",
    "haha" : "하하하하하ㅏ하"
}

print("문서 전체 : ", document)
print("출처 : ", document["source"])
print("내용 : ", document["content"])
print("웃음 : ", document["haha"])

print("-" * 40)

document = [
    {
         "source" : "company_policy.txt",
         "content": "연차 사용은 최소 3일 전에 팀장에게 신청해야 한다."
    },

    {
        "source" : "meeting_note.txt",
        "content" :"초기 버전은 txt 문서 검색부터 구현한다."
    },

    {
        "source" : "faq,txt",
        "content" :"이 서비스는 회사 문서를 기반으로 답변하는 Ai agent 서비스 입니다."
    },
    
    {
    "source" :"faa.txt",
    "content" : "내용내용"
    }   
]

print("첫 번쨰 문서 : ", document[0])
print("첫 번째 문서 출처  : ", document[0]["source"])
print("첫 번째 문서 내용 : ", document[0]["content"])
print("네 번째 문서 내용 : ", document[3]["content"])
print("총 문서 수 : ", len(document))

print("-" *40)

for doc in document:
    print("출처 : " ,doc["source"])
    print("내용 : " ,doc["content"])
    print("내용길이 : ", len(doc["content"]))
    print()


print("-" *40)

def print_document(doc):
    print("[문서 출력]")
    print("출처 : ", doc["source"])
    print("내용 ㅣ ", doc["content"])

print_document(document[0])
print_document(document[1])
