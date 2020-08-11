#!/usr/bin/python3
"""adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

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
    new_state = State(id='6', name='Louisiana')
    session.add(new_state)
    session.commit()
    state = session.query(State).filter_by(name='Louisiana').first()
    print(str(state.id))
    session.close()
