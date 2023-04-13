from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ChatData(Base):
    __tablename__ = "chat_data"

    id = Column(Integer, primary_key=True)
    responses = Column(Text)
    analysis = Column(Text)

engine = create_engine("sqlite:///chat_data.db")
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)