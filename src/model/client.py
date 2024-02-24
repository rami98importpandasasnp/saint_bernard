from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ClientBase(BaseModel):
    name: int
    fiscale_code: int
    address: float


class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
