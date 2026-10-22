import os
import certifi
from pydantic_settings import BaseSettings, SettingsConfigDict

# Fall back to certifi's CA bundle when SSL_CERT_FILE is unset or points to a missing file
ssl_cert = os.environ.get('SSL_CERT_FILE')
if not ssl_cert or not os.path.exists(ssl_cert):
    os.environ['SSL_CERT_FILE'] = certifi.where()


class Settings(BaseSettings):
    openai_api_key: str = ''
    pinecone_api_key: str = ''
    tavily_api_key: str = ''
    pinecone_index: str = 'medical-agent-demo'
    openai_chat_model: str = 'gpt-4.1-mini'
    openai_embed_model: str = 'text-embedding-3-small'
    openai_vision_model: str = 'gpt-4.1-mini'
    api_token: str = ''
    allowed_origins: str = '*'

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    @property
    def allowed_origins_list(self) -> list[str]:
        return [o.strip() for o in self.allowed_origins.split(',') if o.strip()]


settings = Settings()
