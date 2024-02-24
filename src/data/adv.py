from .base import db
from model.adv import Adv
from error import Missing, Duplicate
from .price import Adv


def get_all() -> list[Adv]:
    res = db.query(Adv).all()
    return res
