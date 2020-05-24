from sqlalchemy import (Column, Integer, String, create_engine, event)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:////Users/pranav/learning_plan/learn_sql_alchemy/learn_alembic/data.db', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Image(Base):
    __tablename__ = 'images'
    id          =   Column(Integer, primary_key=True)
    name = Column(String)
    idq = Column(Integer)
    some_random_thing = Column(String)

@event.listens_for(Image, 'after_insert')
def recieve_before_insert(mapper, connection, target):
    print("\n \n \n \n#######An object has been inserted")
    print("mapper:")
    print(mapper)
    print("connection:")
    print(connection)
    print("target:")
    print(target)
    print("####### \n \n \n")

@event.listens_for(Image, 'after_update')
def reciever_after_update(mapper, connection, target):
    print("\n \n \n #######After update")
    print("mapper:")
    print(mapper)
    print("connection:")
    print(connection)
    print("target:")
    print(target)
    print("####### \n \n \n")