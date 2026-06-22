from pathlib import Path

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


def main():
    documents = load_documents()

    print("문서 로드 완료")
    print(f"총 문서 수: {len(documents)}개")

    for doc in documents:
        print("-" * 40)
        print(f"출처: {doc['source']}")
        print(doc["content"][:100])


if __name__ == "__main__":
    main()