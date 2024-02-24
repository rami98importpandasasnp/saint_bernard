from pydantic import BaseModel


class Adv(BaseModel):
    category: str
    sub_category: str
    name: str
    description: str
    game_time: str
    platform: str
