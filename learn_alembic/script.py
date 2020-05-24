from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Image

engine = create_engine('sqlite:////Users/pranav/learning_plan/learn_sql_alchemy/learn_alembic/data.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
simple_object = Image(id=1, name="abcdef")
session.add(simple_object)
#session.commit()
simple_object = session.query(Image).filter_by(name='abcdef').first()
simple_object.name = 'abcd'
session.add(simple_object)
session.commit()
print(simple_object)

