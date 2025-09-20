from langchain_ollama import OllamaLLM

def get_llm(provider="ollama", model="artifish/llama3.2-uncensored"):
    if provider == "ollama":
        return OllamaLLM(model=model)
    raise NotImplementedError(f"Provider {provider} not implemented")
