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

    for chunk in chunks:
        print("-" * 40)
        print(f"출처: {chunk['source']}")
        print(f"chunk 번호: {chunk['chunk_id']}")
        print(chunk["content"][:120])


if __name__ == "__main__":
    main()