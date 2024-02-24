from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AdvBase(BaseModel):
    category: Optional[str]
    sub_category: Optional[str]
    name: str
    description: str
    game_time: Optional[str]
    duration: Optional[int]
    visibility: Optional[int]
    engagement: Optional[int]
    grade: Optional[float]


class AdvCreate(AdvBase):
    pass


class Adv(AdvBase):
    id: int
    platform_id: Optional[int]
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
