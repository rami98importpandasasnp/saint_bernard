from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class SaleBase(BaseModel):
    amount: int
    price: float


class SaleCreate(SaleBase):
    pass


class Sale(SaleBase):
    id: int
    client_id: int
    adv_id: int
    created_at: Optional[datetime]

    class Config:
        orm_mode = True
