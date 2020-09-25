from sqlalchemy import create_engine
# from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

from models import Base, Goods

PATH = 'database/db.sqlite3'


class Repository:
    def __init__(self, path_db):
        self.engine = create_engine(
            f'sqlite:///{path_db}?check_same_thread=False'
        )
        self.create_base()
        self.session = self.get_session()
        # self.session.execute('PRAGMA foreign_keys=ON')

    def create_base(self):
        Base.metadata.create_all(self.engine)

    def get_session(self):
        session = sessionmaker(bind=self.engine)
        session = session()
        return session


if __name__ == "__main__":
    DB = Repository(PATH)
    DB.session.add(Goods('asd'))
    DB.session.commit()
    # print(DB.session.query(Goods).all())
