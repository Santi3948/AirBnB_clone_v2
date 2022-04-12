#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = "states"
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
    @property
    def cities(self):
        return self.cities.format(State.id == state_id)
