from pathlib import Path

def load_documents(data_path: str):
    documents = []

    for file in Path(data_path).glob("*.txt"):
        text = file.read_text(encoding="utf-8")

        documents.append({
            "text": text,
            "source": file.name
        })

    return documents