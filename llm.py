from langchain_openai import ChatOpenAI

def get_llm(temperature : int = 0.0 , max_tokens : int = 512):
    return ChatOpenAI(
        model = "local model",
        base_url="http://127.0.0.1:8080/v1",
        api_key="not-needed",
        temperature=temperature,
        max_tokens = max_tokens,
    )