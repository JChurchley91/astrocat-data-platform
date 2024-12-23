from sqlalchemy import create_engine
import os

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


def get_postgresql_engine() -> create_engine:
    """
    Connect to a PostgreSQL database using SQLAlchemy.
    """
    connection_string = (
        f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )
    engine = create_engine(connection_string)
    return engine
