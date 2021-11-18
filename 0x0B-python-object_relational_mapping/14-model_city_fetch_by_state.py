#!/usr/bin/python3
'''orm module'''


from model_city import City


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

    # initialize orm
    [engine, session] = get_orm_argv()
    Base.metadata.create_all(engine)

    query = session.query(State, City)
    query = query.join(City, State.id == City.state_id)

    for row in query.order_by(City.id):  # print result
        print("{}: ({}) {}".format(
            row.State.name, row.City.id, row.City.name))

    session.close()  # close connection
