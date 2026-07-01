# Company Docs RAG Agent

회사 문서 기반 LLM/RAG AI Agent 프로젝트입니다.

사용자가 회사 문서에 대해 질문하면, 시스템이 관련 문서 조각을 검색하고 출처와 함께 결과를 제공합니다.
현재 버전은 LLM 답변 생성 전 단계로, **TF-IDF 기반 문서 검색 기능**을 구현했습니다.

---

## Project Goal

이 프로젝트의 목표는 회사 내부 문서, 회의록, FAQ, 매뉴얼, 이메일 예시 등을 기반으로 사용자의 질문에 답변할 수 있는 RAG 기반 AI Agent를 구현하는 것입니다.

최종 목표는 다음과 같습니다.

```txt
회사 문서 업로드
→ 문서 chunk 분할
→ 문서 검색
→ LLM 기반 답변 생성
→ 출처 표시
→ 업무 자동화 Agent 기능 추가
```

---

## Motivation

일반 LLM은 회사 내부 문서나 최신 업무 문서를 알지 못합니다.
따라서 회사 문서를 검색한 뒤, 검색된 문서를 근거로 답변하는 RAG 구조가 필요합니다.

이 프로젝트는 실제 기업 업무에서 사용할 수 있는 AI 기능을 직접 설계하고 구현하는 것을 목표로 합니다.

---

## Current Features

현재 구현된 기능은 다음과 같습니다.

```txt
문서 로드
문서 chunk 분할
사용자 질문 입력
TF-IDF 기반 문서 벡터화
Cosine Similarity 기반 유사도 계산
Top-k 관련 문서 검색
문서 출처 표시
chunk 번호 표시
유사도 점수 출력
```

---

## Tech Stack

```txt
Python
scikit-learn
TF-IDF
Cosine Similarity
Pathlib
```

추후 추가 예정 기술:

```txt
FastAPI
LLM API
Embedding
Vector DB
AI Agent
```

---

## Project Structure

```txt
company-docs-rag-agent/
├─ README.md
├─ requirements.txt
├─ sample_docs/
│  ├─ company_policy.txt
│  ├─ meeting_note.txt
│  ├─ faq.txt
│  ├─ service_manual.txt
│  └─ email_sample.txt
├─ src/
│  ├─ main.py
│  └─ search.py
└─ practice/
   ├─ day03_knn_basic.py
   ├─ day05_sklearn_knn.py
   ├─ day06_iris_knn.py
   ├─ day07_decision_tree.py
   ├─ day08_logistic_regression.py
   ├─ day09_linear_regression.py
   ├─ day10_multiple_linear_regression.py
   ├─ day11_pandas_basic.py
   ├─ day12_pandas_csv.py
   ├─ day13_missing_values.py
   ├─ day14_pandas_filtering.py
   ├─ day15_pandas_train_test_split.py
   ├─ day16_pandas_classification.py
   └─ day17_tfidf_search.py
```

---

## How It Works

현재 시스템은 다음 흐름으로 동작합니다.

```txt
1. sample_docs 폴더의 txt 문서를 불러온다.
2. 문서를 문단 단위로 chunk로 나눈다.
3. 사용자가 질문을 입력한다.
4. 각 chunk와 사용자 질문을 TF-IDF 벡터로 변환한다.
5. Cosine Similarity로 질문과 chunk의 유사도를 계산한다.
6. 유사도가 높은 상위 문서를 출력한다.
7. 문서 이름, chunk 번호, 내용, 유사도 점수를 함께 보여준다.
```

---

## Example

### User Question

```txt
고객 문의에는 어떻게 답변해?
```

### Search Result

```txt
1위
문서: email_sample.txt
chunk 번호: 2
내용:
고객 문의에 대한 답변 이메일 초안을 작성해야 한다.
고객이 서비스 사용 방법을 문의하면, 담당자는 정중하게 사용 방법을 안내한다.
이메일에는 문의 내용에 대한 답변, 추가 안내, 감사 인사를 포함한다.

유사도 점수: 0.3012
```

---

## Another Example

### User Question

```txt
연차 정책이 어떻게 돼?
```

### Search Result

```txt
문서: company_policy.txt
chunk 번호: 1
내용:
우리 회사의 연차 정책은 다음과 같다.
신입사원은 입사 후 1개월 개근 시 1일의 연차가 발생한다.
1년 이상 근무한 직원은 근로기준법에 따라 15일의 연차를 사용할 수 있다.
연차 사용은 최소 3일 전에 팀장에게 신청해야 한다.
```

---

## Why TF-IDF?

현재 버전에서는 RAG 검색 구조를 이해하기 위해 TF-IDF를 사용했습니다.

TF-IDF는 문서와 질문을 숫자 벡터로 변환하고, Cosine Similarity를 통해 질문과 가장 관련 있는 문서를 찾는 방식입니다.

한국어 검색 성능을 개선하기 위해 기본 단어 단위 분석 대신 character-level n-gram 방식을 사용했습니다.

```python
TfidfVectorizer(analyzer="char", ngram_range=(2, 3))
```

이를 통해 `광수`, `광수는`, `광수가`처럼 조사 차이로 인해 검색이 실패하는 문제를 일부 완화했습니다.

---

## What I Learned

이 프로젝트를 구현하면서 다음 내용을 학습했습니다.

```txt
Python 파일 처리
리스트와 딕셔너리 구조
문서 chunk 분할
TF-IDF 벡터화
Cosine Similarity
Top-k 검색
검색 품질과 문서 품질의 관계
RAG의 Retrieval 단계
```

또한 머신러닝 기초 학습을 위해 다음 실습을 진행했습니다.

```txt
KNN 직접 구현
KNN with scikit-learn
Decision Tree
Logistic Regression
Linear Regression
Multiple Linear Regression
Pandas DataFrame
CSV 불러오기
결측치 처리
조건 필터링
Pandas + train_test_split
Pandas + Classification
```

---

## Current Status

현재 프로젝트 상태:

```txt
RAG 검색 파트 v0.1 구현 완료
LLM 답변 생성 기능은 아직 미구현
출처 기반 검색 결과 출력 가능
Top-k 관련 문서 검색 가능
```

---

## Next Steps

다음 단계는 다음과 같습니다.

```txt
1. 검색 결과 기반 간단 답변 생성 함수 추가
2. LLM API 연결
3. 출처 기반 답변 생성
4. FastAPI 서버 구현
5. 문서 업로드 기능 추가
6. Embedding 기반 검색으로 개선
7. Vector DB 연결
8. AI Agent 기능 추가
```

추가할 AI Agent 기능 예시:

```txt
회의록에서 액션 아이템 추출
FAQ 자동 생성
문서 요약
이메일 초안 작성
정책 문서 비교
업무 체크리스트 생성
```

---

## Long-term Direction

이 프로젝트는 단순 문서 검색기가 아니라, 회사 문서를 기반으로 업무를 자동화하는 AI Agent로 확장하는 것을 목표로 합니다.

최종적으로는 다음과 같은 시스템을 목표로 합니다.

```txt
사용자 질문
→ 관련 문서 검색
→ LLM 기반 답변 생성
→ 출처 표시
→ 필요한 업무 액션 수행
```

예시:

```txt
회의록에서 할 일을 추출해줘.
정책 문서를 요약해줘.
고객 문의에 대한 이메일 초안을 작성해줘.
FAQ를 자동으로 만들어줘.
```

---

## Personal Goal

저는 모바일 앱과 서비스 개발 경험을 바탕으로, LLM/RAG 기반 AI Agent를 실제 서비스와 업무 자동화에 적용하는 AI 엔지니어를 목표로 합니다.

이 프로젝트는 그 목표를 위해 Python, 머신러닝, NLP, RAG, AI Agent 구조를 단계적으로 학습하고 구현하는 포트폴리오 프로젝트입니다.
