import json
from datetime import datetime
from pathlib import Path


LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "query_history.jsonl"


def save_query_history(query, search_results, answer):
    LOG_DIR.mkdir(exist_ok=True)

    history_item = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "query": query,
        "search_results": [],
        "search_result_count" : len(search_results),
        "answer": answer,
        
    }

    for item in search_results:
        document = item["document"]
        score = item["score"]

        history_item["search_results"].append({
            "rank":item["rank"],
            "source": document["source"],
            "chunk_id": document["chunk_id"],
            "content": document["content"],
            "score": float(score),
        })

    with LOG_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(history_item, ensure_ascii=False) + "\n")