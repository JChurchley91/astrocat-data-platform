from astrocat.utils.db_utils import get_postgresql_engine
from dagster import job, op
from sqlalchemy import text


@op
def create_config_schema() -> str:
    """
    Create the config schema in the PostgreSQL database.
    :return: A message indicating whether the schema was created successfully.
    """
    engine = get_postgresql_engine()
    connection = engine.connect()

    try:
        connection.execute(text(f"CREATE SCHEMA IF NOT EXISTS astrocat_config"))
        connection.commit()
        return "Schema created successfully"

    except Exception as e:
        return f"Failed to create schema - {e}"
    finally:
        connection.close()
        engine.dispose()


@job
def create_astrocat_config_schema():
    create_config_schema()


@job
def create_astrocat_config_table():
    pass
