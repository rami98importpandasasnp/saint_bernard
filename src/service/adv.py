import os
from model.adv import Adv
from data import adv as data


def get_all() -> list[Adv]:
    return data.get_all()
