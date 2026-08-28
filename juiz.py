from deepeval.models import OllamaModel 
import os

def obter_juiz():
    provider = os.getenv("JUIZ_PROVIDER", "ollama").lower()

    return OllamaModel(
        model=os.getenv("JUIZ_MODEL", "llama3.2:3b"),
        base_url=os.getenv("OLLAMA_URL", "http://localhost:11434"),
    )