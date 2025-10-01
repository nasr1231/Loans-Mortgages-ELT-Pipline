from sqlalchemy import create_engine,text
from sqlalchemy.exc import SQLAlchemyError
import logging


def postgres_connection(host, db_name, user, password):

    # connection_string = conn_string
    connection_string = f'postgresql://{user}:{password}@{host}/{db_name}'

    try:
        engine = create_engine(connection_string)
        postgresql_conn = engine.connect()
        
        ### Logging Connection Status
        logging.info("Connected to PostgreSQL db successfully")
        return postgresql_conn, engine
    
    except SQLAlchemyError as error:
        logging.error("Error while connecting to PostgreSQL: %s", error)
        return None, None
    
def close_connection(connection, engine):
    if connection:
        connection.close()
        logging.info("connection is closed")
    if engine:
        engine.dispose()
        logging.info("SQLAlchemy engine disposed")
