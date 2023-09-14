from typing import Optional, List

from pydantic import BaseModel, EmailStr

from schemas.artigo_schema import ArtigoSchema


# Não retornar senha
class UsuarioSchemaBase(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    email: EmailStr
    eh_admin: bool = False
    
    class Config:
        orm_mode = True
        
#usado para criar a conta
class UsuarioSchemaCreate(UsuarioSchemaBase):
    senha: str
    
 #retorna usuario mais artigo   
class UsuarioSchemaArtigos(UsuarioSchemaBase):
    artigos: Optional[List[ArtigoSchema]]
    
 #Atualizar usuario   
class UsuarioSchemaUp(UsuarioSchemaBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]
    senha: Optional[str]
    eh_admin: Optional[bool]
