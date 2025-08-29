import requests
from config import GRAPHQL_URL

async def run_query(query: str, variables: dict = None):
    response = requests.post(
        GRAPHQL_URL,
        json={"query": query, "variables": variables or {}}
    )

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Query falhou: {response.status_code} - {response.text}")
