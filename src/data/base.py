"""Initialize SQLite database"""

import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm.session import Session

db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_name = os.environ.get("DB_NAME")
pricing_db_conn = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}"

# Create the engine
engine = create_engine(pricing_db_conn)

# Create a session class
Session = sessionmaker(bind=engine)

# Create a session
session = Session()


class AlphaQueryFinanceQuerier:
    def _init_(self, db=session()) -> None:
        self.db = db

    def _close(self):
        if self.db:
            self.db.close()
            self.db = None

    def _del_(self):
        self._close()

    def close_connection_if_exception(func):
        def inner_function(self, *args, **kwargs):
            try:
                value = func(self, *args, **kwargs)
                return value
            except Exception as e:
                self._close()
                raise e

        return inner_function

    def update_entity_to_db(self, dto_entity, db_entity):
        for key in dto_entity._dict_.keys():
            if key != "id" and key != "create_timestamp":
                value = getattr(dto_entity, key)
                old_value = getattr(db_entity, key)
                if value != old_value:
                    setattr(db_entity, key, value)
        return db_entity
