#!/usr/bin/python3
"""DBStorage module"""
from sqlalchemy import create_engine, MetaData
from os import getenv
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.sql import text
from models.base_model import Base, BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.review import Review
from models.user import User

class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(
        "mysql+mysqldb://{}:{}@{}/{}".format(
        getenv("HBNB_MYSQL_USER"),
        getenv("HBNB_MYSQL_PWD"),
        getenv("HBNB_MYSQL_HOST"),
        getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if getenv("HBNB_MYSQL_DB") == "test":
             m = MetaData(engine)
             meta.reflect()
             meta.drop_all()

    def all(self, cls=None):
        lis = ["User", "State", "City", "Amenity", "Place", "Review"]
        di = {}
        self.__session = Session(bind=self.__engine)
        if cls in lis:
            for instance in self.__session.query(text(cls)):
                di[cls + "." + instance.id] = instance
        return di

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None): 
        self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session_1 = sessionmaker(self.__engine)
        Session_2 = scoped_session(Session_1)
        self.__session =  Session_2(bind=self.__engine, expire_on_commit=False)
