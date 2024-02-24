from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InventoryBase(BaseModel):
    grade: int
    price: float


class InventoryCreate(InventoryBase):
    pass


class Inventory(InventoryBase):
    id: int
    adv_id: int
    client_id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
