#!/usr/bin/python3
"""
This script adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Adds 'Louisiana' to the states table and prints the new state's id.
    """

    db_url = f"mysql+mysqldb://{{}}:{{}}@localhost:3306/{{}}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)
