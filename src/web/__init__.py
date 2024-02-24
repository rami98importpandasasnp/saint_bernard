import os
from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.templating import Jinja2Templates

from model.creature import Creature

if os.getenv("CRYPTID_UNIT_TEST"):
    from fake import creature as service
else:
    from service import creature as service
from error import Missing, Duplicate

router = APIRouter(prefix="/creature")
top = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=f"{top}/template")
