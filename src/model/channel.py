from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ChannelBase(BaseModel):
    posts: Optional[int]
    likes: Optional[int]
    comments: Optional[int]
    interactions: Optional[int]
    reactions: Optional[int]


class ChannelCreate(ChannelBase):
    pass


class Channel(ChannelBase):
    id: int
    client_id: int
    platform_id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
