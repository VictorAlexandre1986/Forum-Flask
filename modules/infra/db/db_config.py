import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self):
        self.__connection_string = f"{os.getenv('DB_URL')}" if os.getenv('DB_URL') else 'sqlite:///backend_test.db'
        self.session = None

    def get_engine(self):
        """Return connection Engine
        :parram - None
        :return - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine

    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()  # pylint: disable=no-member
