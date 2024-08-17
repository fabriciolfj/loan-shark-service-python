import configparser

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class UnitOfWork:

    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')

        db_url = config['database']['url']
        self.session = Session(create_engine(db_url))

    def commit(self):
        self.session.commit()
