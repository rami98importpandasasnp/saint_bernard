import os
from fastapi import APIRouter, HTTPException
from model.channel import Channel
from service import channel as service
from error import Duplicate, Missing

router = APIRouter(prefix="/channel")


@router.get("/{client_id}")
def get_all_channel_by_client(client_id: int) -> list[Channel]:
    return service.get_all_channel_by_client(client_id)


@router.get("/{name}")
def get_channel(name) -> list[Channel]:
    return service.get_channel(name)
