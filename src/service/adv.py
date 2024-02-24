import os
from model.adv import Adv
from data import adv as data


def get_all() -> list[Adv]:
    return data.get_all()


def get_one(name: str) -> Explorer:
    return data.get_one(name)


def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)


def modify(name: str, explorer: Explorer) -> Explorer:
    return data.modify(name, explorer)


def delete(name: str):
    return data.delete(name)
