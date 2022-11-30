from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Pudge(Base):
    __tablename__ = 'pudge'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)

    def __repr__(self) -> str:
        return self.title


class Word(Base):
    __tablename__ = 'word'
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    count = Column(Integer, default=1)

    def __repr__(self) -> str:
        return f'Слово: {self.title} было использовано {self.count}'
