#!/usr/bin/python3
"""prints the State object with the name passed as argument"""

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
    state_id = session.query(State).filter_by(name=argv[4]).first()
    if state_id:
        print("{}".format(state_id.id))
    else:
        print("Not found")
    session.close()
