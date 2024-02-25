import os
from model.channel import Channel
from data import channel as data


def get_all_channel_by_client(client_id: int) -> list[Channel]:
    return data.get_all_channel_by_client(client_id)


def get_single_channel_by_client(client_id: int, channel: str) -> Channel:
    return data.get_single_channel_by_client(client_id, channel)
