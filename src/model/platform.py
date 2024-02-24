from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PlatformBase(BaseModel):
    name: str


class PlatformCreate(PlatformBase):
    pass


class Platform(PlatformBase):
    id: int

    class Config:
        orm_mode = True
