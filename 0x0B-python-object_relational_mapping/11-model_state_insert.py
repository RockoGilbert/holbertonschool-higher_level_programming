#!/usr/bin/python3
'''orm module'''


def get_orm_argv():
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    return [engine, session]


if __name__ == '__main__':
    from sqlalchemy.engine import create_engine
    from sqlalchemy.orm.session import sessionmaker
    from model_state import State
    from model_state import Base, State
    from sys import argv

    [engine, session] = get_orm_argv()
    Base.metadata.create_all(engine)
    new_state = State(name="Louisiana")
    query = session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
    