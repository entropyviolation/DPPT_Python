import os
from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ChatData(Base):
    __tablename__ = "chat_data"

    id = Column(Integer, primary_key=True)
    responses = Column(Text)
    analysis = Column(Text)

# Get the database URL from the environment variable
database_url = os.environ['postgres://fobglwnekkiazp:d39c346a5fd7173d11de2f75081b0cf04de82e443cb96102f890d6d4ce93cbcb@ec2-3-92-151-217.compute-1.amazonaws.com:5432/dbdlppji0fu42o']

engine = create_engine(database_url)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
