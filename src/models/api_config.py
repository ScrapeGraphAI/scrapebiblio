from dataclasses import dataclass
from typing import Optional

@dataclass
class APIConfig:
    openai_api_key: str
    semantic_scholar_api_key: str
    core_api_key: Optional[str] = None
    base_api_key: Optional[str] = None
