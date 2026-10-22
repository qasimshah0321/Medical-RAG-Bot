from app.config import settings


def mask(value: str) -> str:
    return f"{value[:4]}...{value[-4:]}" if len(value) > 8 else ('<set>' if value else '<missing>')


print(f"OpenAI API Key:   {mask(settings.openai_api_key)}")
print(f"Pinecone API Key: {mask(settings.pinecone_api_key)}")
print(f"Tavily API Key:   {mask(settings.tavily_api_key)}")
print(f"Pinecone index:   {settings.pinecone_index}")
print(f"Chat model:       {settings.openai_chat_model}")
print(f"Embed model:      {settings.openai_embed_model}")
print(f"Vision model:     {settings.openai_vision_model}")
print(f"Allowed origins:  {settings.allowed_origins_list}")
