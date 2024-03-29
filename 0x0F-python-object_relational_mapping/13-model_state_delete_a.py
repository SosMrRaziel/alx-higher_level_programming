#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Deletes states with a name containing the letter 'a'.
    """

    db_url = f"mysql+mysqldb://{{}}:{{}}@localhost:3306/{{}}".format(
        argv[1], argv[2], argv[3])
    engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    session.commit()
