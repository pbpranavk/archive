from datetime import datetime, timedelta

from sqlalchemy import (Column, DateTime, ForeignKey, Integer, String, Table,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, relationship, sessionmaker


engine = create_engine('sqlite:////Users/pranav/pythonL/learn_sql_alchemy/data2.db', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    user_name = Column(String)
    first_name = Column(String)
    last_name = Column(String)

    def __repr__(self):
        return "<User (id='%s', username='%s', firstname='%s', lastname='%s')"%(self.id, self.user_name, self.first_name, self.last_name)

class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    created_user = relationship("user",backref="question",lazy="dynamic")

    def __repr__(self):
        return "<Question (id='%s', title='%s', description='%s')"%(self.id, self.title, self.description)

class Answer(Base):
    __tablename__ = "answer"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    question_id = relationship("question", backref="answer", lazy="dynamic")
    created_user = relationship("user",backref="answer",lazy="dynamic")

class Comment(Base):
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    answer_id = relationship("answer", backref="comment", lazy="dynamic")
    created_user = relationship("user",backref="comment",lazy="dynamic")

votes = Table("answer_comment_vote", Base.metadata,
    Column("join_id", primary_key=True),
    Column("id", Integer), #Answer or Comment id determined by category column.
    Column("category", String),
    Column("user_id", Integer, ForeignKey("user.id")),
    Column("vote_type",Integer) #upvote = 1 and downvote = -1
)

session = Session()
