from .base import db
from model.channel import Channel
from error import Missing, Duplicate
from .price import Channel, Platform


def get_all_channel_by_client(client_id: int) -> list[Channel]:
    res = db.query(Channel).filter(Channel.client_id == client_id).all()
    return res


def get_channel(name: str) -> Channel:
    res = (
        db.query(Channel)
        .join(Platform, Channel.platform_id == Platform.id)
        .filter(Platform.name == name)
    ).all()
    return res
