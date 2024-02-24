from sqlalchemy import Column, ForeignKey, Integer, String, Text, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Client(Base):
    __tablename__ = "client"
    __table_args__ = {"schema": "price"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Integer, nullable=False)
    fiscale_code = Column(Integer, nullable=False)
    address = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)


class Platform(Base):
    __tablename__ = "platform"
    __table_args__ = {"schema": "price"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)


class Channel(Base):
    __tablename__ = "channel"
    __table_args__ = {"schema": "price"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("price.client.id"), nullable=False)
    platform_id = Column(Integer, ForeignKey("price.platform.id"), nullable=False)
    posts = Column(Integer, nullable=True)
    likes = Column(Integer, nullable=True)
    comments = Column(Integer, nullable=True)
    interactions = Column(Integer, nullable=True)
    reactions = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=False)

    client = relationship("Client")
    platform = relationship("Platform")


class Adv(Base):
    __tablename__ = "adv"
    __table_args__ = {"schema": "price"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(Text, nullable=True)
    sub_category = Column(Text, nullable=True)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    game_time = Column(Text, nullable=True)
    platform_id = Column(Integer, ForeignKey("price.platform.id"), nullable=True)
    duration = Column(Integer, nullable=True)
    visibility = Column(Integer, nullable=True)
    engagement = Column(Integer, nullable=True)
    grade = Column(Float, nullable=True)
    created_at = Column(DateTime, nullable=False)

    platform = relationship("Platform")


class Sale(Base):
    __tablename__ = "sale"
    __table_args__ = {"schema": "price"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    client_id = Column(Integer, ForeignKey("price.client.id"), nullable=False)
    adv_id = Column(Integer, ForeignKey("price.adv.id"), nullable=False)
    amount = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)

    client = relationship("Client")
    adv = relationship("Adv")


class Inventory(Base):
    __tablename__ = "inventory"
    __table_args__ = {"schema": "price"}

    id = Column(Integer, primary_key=True, autoincrement=True)
    adv_id = Column(Integer, ForeignKey("price.adv.id"), nullable=False)
    client_id = Column(Integer, ForeignKey("price.client.id"), nullable=False)
    grade = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False)

    adv = relationship("Adv")
    client = relationship("Client")
