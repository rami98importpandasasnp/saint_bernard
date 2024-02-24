"""Initialize SQLite database"""

import os
from pathlib import Path
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm.session import Session
from sqlalchemy.ext.declarative import declarative_base

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
db = Session()
Base = declarative_base()
