#!/usr/bin/python3
"""deletes all State objects with a name containing the letter a"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()
    a_state_a = session.query(State)
    state_a = a_state_a.filter(State.name.like('%a%')).order_by(State.id)
    for state in state_a:
        session.delete(state)
    session.commit()
    session.close()
