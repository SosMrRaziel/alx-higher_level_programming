#!/usr/bin/python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id).all():
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
