#!/usr/bin/python3
"""
Contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

class City(Base):
    """Attributes of the City class:
    id: An integer that serves as the unique identifier for each city.
    It is auto-generated, cannot be null,
    and is set as the primary key of the table.
    name: A string of up to 128 characters
    that represents the name of the city.
    This attribute cannot be null.
    state_id: An integer that acts as a foreign
    key to the id attribute of the states table.
    It cannot be null and establishes a relationship
    between each city and its corresponding state."""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True,
                nullable=False, autoincrement="auto")
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
