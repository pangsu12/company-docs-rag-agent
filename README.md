# Company Docs RAG Agent

회사 문서를 기반으로 사용자의 질문에 관련된 문서 조각을 검색하고, 출처와 함께 답변을 생성하는 RAG 기반 AI Agent 프로젝트입니다.

현재 버전은 TF-IDF 기반 Retrieval, 검색 결과 기반 답변 생성, OpenAI API 연결 구조, fallback 답변 처리, 질문 기록 저장, 그리고 간단한 Agent 기능을 포함합니다.

---

## 프로젝트 목표

이 프로젝트의 최종 목표는 회사 문서나 서비스 데이터를 기반으로 사용자의 질문에 답하고, 문서 요약, 회의록 액션 아이템 추출, 이메일 초안 작성 같은 업무 기능까지 수행하는 LLM/RAG 기반 AI Agent 서비스를 구현하는 것입니다.

현재는 RAG 구조의 핵심 흐름을 직접 구현하는 데 집중하고 있습니다.

---

## 현재 구현된 기능

### 1. 문서 로드

`sample_docs` 폴더 안의 `.txt` 문서를 읽어옵니다.

```txt
sample_docs/
├── company_policy.txt
├── email_sample.txt
├── faq.txt
├── meeting_note.txt
└── service_manual.txt
```

각 문서는 다음 형태로 저장됩니다.

```python
{
    "source": "company_policy.txt",
    "content": "문서 내용..."
}
```

---

### 2. 문서 Chunk 분할

문서 내용을 빈 줄 기준으로 나누어 chunk 단위로 저장합니다.

```python
{
    "source": "company_policy.txt",
    "chunk_id": 1,
    "content": "우리 회사의 연차 정책은 다음과 같다..."
}
```

문서를 chunk로 나누는 이유는 긴 문서 전체를 검색하는 것보다, 질문과 관련 있는 작은 문서 조각을 찾는 것이 더 정확하기 때문입니다.

---

### 3. TF-IDF 기반 문서 검색

사용자 질문과 각 문서 chunk를 TF-IDF 벡터로 변환합니다.

현재 한국어 검색을 위해 character-level n-gram 방식을 사용합니다.

```python
TfidfVectorizer(analyzer="char", ngram_range=(2, 3))
```

이후 cosine similarity를 계산해 질문과 가장 관련 있는 chunk를 찾습니다.

```txt
사용자 질문
→ TF-IDF 벡터화
→ 문서 chunk와 유사도 계산
→ top-k 관련 문서 반환
```

---

### 4. 낮은 유사도 필터링

관련성이 낮은 검색 결과는 제외합니다.

```python
min_score=0.08
```

예를 들어 회사 문서와 관련 없는 질문은 검색 결과에서 제외됩니다.

```txt
질문: 피자 추천해줘
→ 관련 문서를 찾지 못했습니다.
```

---

### 5. 인사말 처리

단순 인사말은 문서 검색을 실행하지 않고 안내 답변을 반환합니다.

```txt
질문: 안녕하세요
답변: 안녕하세요. 회사 문서에 대해 궁금한 내용을 질문해주세요.
```

---

### 6. OpenAI API 답변 생성 구조

검색된 top-k 문서를 context로 구성하고, OpenAI API에 전달해 답변을 생성할 수 있는 구조를 추가했습니다.

```txt
검색 결과 top-k
→ context 구성
→ prompt 생성
→ OpenAI API 호출
→ 문서 기반 답변 생성
```

현재는 API 키가 없거나 API 호출에 실패하면 fallback 답변을 사용합니다.

```txt
OpenAI API 키 없음
→ fallback 답변 사용
```

이 구조를 통해 API 오류가 발생해도 프로그램이 중단되지 않습니다.

---

### 7. Fallback 답변 생성

OpenAI API를 사용할 수 없는 경우, 가장 관련 있는 문서 chunk를 기반으로 답변을 생성합니다.

예시:

```txt
질문 : 연차 정책이 궁금해

관련 문서에 따르면:
우리 회사의 연차 정책은 다음과 같다.
신입사원은 입사 후 1개월 개근 시 1일의 연차가 발생한다.
1년 이상 근무한 직원은 근로기준법에 따라 15일의 연차를 사용할 수 있다.
연차 사용은 최소 3일 전에 팀장에게 신청해야 한다.

출처 : company_policy.txt, chunk 1
```

---

### 8. 질문 기록 저장

사용자 질문, 검색 결과, 답변, timestamp를 JSONL 형식으로 저장합니다.

저장 위치:

```txt
logs/query_history.jsonl
```

저장 예시:

```json
{
  "timestamp": "2026-07-13T16:10:20",
  "query": "연차 정책이 궁금해",
  "search_results": [
    {
      "source": "company_policy.txt",
      "chunk_id": 1,
      "content": "우리 회사의 연차 정책은 다음과 같다...",
      "score": 0.2511
    }
  ],
  "answer": "질문 : 연차 정책이 궁금해..."
}
```

`logs/` 폴더는 민감한 사용자 질문이 포함될 수 있으므로 GitHub에는 업로드하지 않습니다.

---

### 9. Rule-based Agent 기능

사용자 질문의 의도를 간단히 분류하여 일반 Q&A가 아닌 경우 별도 Agent 기능을 실행합니다.

현재 지원하는 Agent 기능은 다음과 같습니다.

```txt
문서 요약
회의록 기반 액션 아이템 추출
```

질문 의도 분류는 키워드 기반으로 수행합니다.

```txt
"요약", "정리", "핵심"
→ summary

"할 일", "해야 할 일", "액션 아이템", "체크리스트"
→ action_items

그 외
→ 일반 Q&A
```

---

## Agent 기능 예시

### 문서 요약

입력:

```txt
서비스 매뉴얼 요약해줘
```

출력 예시:

```txt
질문 : 서비스 매뉴얼 요약해줘

service_manual.txt 문서 핵심 요약:

1. 사용자는 문서를 업로드한 뒤 질문을 입력할 수 있다. 시스템은 업로드된 문서를 작은 단위로 나누고, 질문과 관련 있는 문서를 검색한다. 검색된 문서를 기반으로 AI가 답변을 생성한다.

출처:
- service_manual.txt, chunk 2
```

---

### 회의록 액션 아이템 추출

입력:

```txt
회의록에서 해야 할 일 정리해줘
```

출력 예시:

```txt
질문 : 회의록에서 해야 할 일 정리해줘

문서에서 추출한 업무 체크리스트는 다음과 같습니다.

1. 초기 버전은 txt 문서 검색부터 구현한다.
2. 이후 PDF 업로드 기능을 추가한다.
3. 답변에는 반드시 출처 문서를 표시한다.

출처:
- meeting_note.txt, chunk 3
```

---

## 프로젝트 구조

```txt
company-docs-rag-agent/
├── sample_docs/
│   ├── company_policy.txt
│   ├── email_sample.txt
│   ├── faq.txt
│   ├── meeting_note.txt
│   └── service_manual.txt
│
├── src/
│   ├── main.py
│   ├── search.py
│   ├── generator.py
│   ├── logger.py
│   └── agent.py
│
├── practice/
├── docs/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 주요 파일 설명

### `src/main.py`

프로젝트의 전체 실행 흐름을 담당합니다.

```txt
문서 로드
→ chunk 분할
→ 사용자 질문 입력
→ 인사말 처리
→ 문서 검색
→ Agent 기능 확인
→ 답변 생성
→ 질문 기록 저장
```

---

### `src/search.py`

TF-IDF와 cosine similarity를 사용해 사용자 질문과 관련 있는 문서 chunk를 검색합니다.

주요 기능:

```txt
TF-IDF 벡터화
cosine similarity 계산
top-k 검색
낮은 유사도 필터링
```

---

### `src/generator.py`

검색 결과를 기반으로 답변을 생성합니다.

주요 기능:

```txt
OpenAI API 답변 생성 구조
fallback 답변 생성
인사말 처리
context 구성
```

---

### `src/logger.py`

질문 기록을 JSONL 파일로 저장합니다.

저장 항목:

```txt
timestamp
query
search_results
answer
```

---

### `src/agent.py`

사용자 질문 의도를 분류하고 Agent 기능을 실행합니다.

현재 기능:

```txt
문서 요약
회의록 액션 아이템 추출
```

---

## 실행 방법

### 1. 패키지 설치

```bash
pip install -r requirements.txt
```

Windows에서 pip 실행이 막힐 경우:

```powershell
python -m pip install -r requirements.txt
```

---

### 2. 환경변수 설정

OpenAI API를 사용할 경우 프로젝트 루트에 `.env` 파일을 생성합니다.

```txt
OPENAI_API_KEY=your_api_key_here
```

API 키가 없는 경우에도 fallback 답변으로 실행됩니다.

`.env` 파일은 GitHub에 업로드하지 않습니다.

---

### 3. 실행

```bash
python src/main.py
```

---

## 테스트 질문

```txt
안녕하세요
```

```txt
연차 정책이 궁금해
```

```txt
고객 문의에는 어떻게 답변해야 해?
```

```txt
서비스 매뉴얼 요약해줘
```

```txt
회의록에서 해야 할 일 정리해줘
```

```txt
피자 추천해줘
```

---

## 현재 버전

```txt
v0.1: TF-IDF 기반 문서 검색
v0.2: 검색 결과 기반 답변 생성
v0.3: 인사말 처리 + 낮은 유사도 필터링
v0.4: OpenAI API 연결 구조 + fallback 처리
v0.5: 질문 기록 저장
v0.6: Rule-based Agent 기능 추가
```

---

## 현재 한계

현재 프로젝트는 아직 초기 버전입니다.

한계는 다음과 같습니다.

```txt
TF-IDF 기반 검색이라 의미 기반 검색에는 한계가 있음
LLM API 결제/키가 없으면 fallback 답변만 사용함
문서 업로드 기능은 아직 없음
Vector DB는 아직 사용하지 않음
FastAPI 서버는 아직 구현하지 않음
Agent 기능은 rule-based 방식임
```

예를 들어 TF-IDF는 단어 또는 글자 조각의 겹침을 기반으로 검색하기 때문에, 동의어나 문맥을 깊게 이해하지 못합니다.

---

## 향후 개선 계획

```txt
1. OpenAI API 정상 연결 후 LLM 기반 답변 생성 강화
2. embedding 기반 semantic search 추가
3. Chroma 또는 FAISS 기반 Vector DB 연결
4. PDF 문서 업로드 기능 추가
5. FastAPI 서버화
6. React Native 또는 Web UI 연결
7. Supabase 기반 사용자별 질문 기록 저장
8. LLM 기반 intent classification 적용
9. 이메일 초안 작성 Agent 기능 추가
10. FAQ 자동 생성 Agent 기능 추가
```

---

## 포트폴리오 설명

이 프로젝트는 회사 문서를 기반으로 사용자 질문에 관련된 문서 chunk를 검색하고, 출처와 함께 답변을 생성하는 RAG 기반 AI Agent 프로젝트입니다.

현재는 TF-IDF와 cosine similarity를 사용해 Retrieval 단계를 직접 구현했으며, OpenAI API 연결 구조와 fallback 답변 생성을 추가했습니다. 또한 사용자 질문 기록을 JSONL 형식으로 저장하고, 문서 요약과 회의록 액션 아이템 추출을 수행하는 rule-based Agent 기능을 구현했습니다.

향후 embedding 기반 semantic search, Vector DB, FastAPI 서버, LLM 기반 Agent 기능으로 확장할 계획입니다.