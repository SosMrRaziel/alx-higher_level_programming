#!/usr/bin/python3
"""
This script prints all City objects from the database hbtn_0e_14_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Base.metadata.create_all(engine)


    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    query = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in query:
        print(f"{state.name}: ({city.id}) {city.name}")
