from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import declarative_base, declared_attr


class PreBase:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)


Base = declarative_base(cls=PreBase)


class Post(Base):
    title = Column(String(200))
    author = Column(String(50))
    content = Column(Text)
    url = Column(String(200))

    def __repr__(self):
        return f"{self.title} by {self.author}"
