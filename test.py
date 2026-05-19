import requests

response = requests.post(
    "http://127.0.0.1:8288/e/rag/query_pdf_ai",
    json={
        "data": {
            "question": "What is this document about?",
            "top_k": 5
        }
    }
)

print("STATUS:", response.status_code)
print("TEXT:")
print(response.text)