import os
from fastapi import APIRouter, HTTPException
from model.adv import Adv
from service import adv as service
from error import Duplicate, Missing

router = APIRouter(prefix="/adv")


@router.get("")
def get_all() -> list[Adv]:
    return service.get_all()
