from .base import db
from model.channel import Channel
from error import Missing, Duplicate
from .price import Channel, Platform


def get_all_channel_by_client(client_id: int) -> list[Channel]:
    res = db.query(Channel).filter(Channel.client_id == client_id).all()
    return res


def get_single_channel_by_client(client_id: int, channel: str) -> Channel:
    res = (
        db.query(
            Channel.id,
            Channel.client_id,
            Channel.platform_id,
            Channel.created_at,
            Channel.posts,
            Channel.likes,
            Channel.comments,
            Channel.interactions,
            Channel.reactions,
        )
        .join(Platform, Channel.platform_id == Platform.id)
        .filter(Channel.client_id == client_id, Platform.name == channel)
    ).first()
    return res
