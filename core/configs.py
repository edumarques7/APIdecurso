from typing import List 
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql://postgres:cujIUJEb0Tkyp2eCzSgh@containers-us-west-181.railway.app:7037/railway"
    DBBaseModel = declarative_base()
    
    JWT_SECRET: str = 'xLgeXKD02H1ksxBJMyC5csII-eU-g58R9EyIP0N67nw'
    """
    import secrets
    
    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM = str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True
        
        
settings: Settings = Settings()

