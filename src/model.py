from pyramid.authorization import Allow, Everyone

from sqlalchemy import (
    Column,
    Integer,
    Text,
    String, 
    ForeignKey, 
    Table
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship


from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import register

DBSession = scoped_session(sessionmaker())
register(DBSession)
Base = declarative_base()


class Page(Base):
    __tablename__ = 'wikipages'

    uid = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)
    owner = relationship('User', uselist=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}



class User(Base):
    __tablename__ = 'users'

    uid = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)

    page_id = Column(Integer, ForeignKey("wikipages.uid"), index=True) 


class Root:
    __acl__ = [(Allow, 1, 'view')]
    def __init__(self, request):
        pass