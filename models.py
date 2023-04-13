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

# Set the DATABASE_URL variable to the connection string
DATABASE_URL = os.environ.get('DATABASE_URL')

# Replace 'postgres://' with 'postgresql://' in the DATABASE_URL
DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
