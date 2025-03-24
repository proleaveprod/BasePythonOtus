from typing import Optional, List
from pydantic import BaseModel

class PowerBase(BaseModel):
    name: str

class PowerCreate(PowerBase):
    pass

class Power(PowerBase):
    id: int
    
    class Config:
        from_attributes = True  # или ранее `orm_mode = True` в Pydantic v1

class CharacterBase(BaseModel):
    name: str
    fullname: Optional[str] = None
    desc: Optional[str] = None
    img_url: Optional[str] = None

class CharacterCreate(CharacterBase):
    powers: List[PowerCreate] = []

class Character(CharacterBase):
    id: int
    powers: List[Power] = []
    
    class Config:
        from_attributes = True