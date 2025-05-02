from aiogram.types import CallbackQuery
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

from loader import dp, bot

engine = create_engine("sqlite:///goldenLike.db")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class VideoProject(Base):
    __tablename__ = "videoproject"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    voices = Column(Integer, nullable=False, default=0)


class UserVote(Base):
    __tablename__ = "user_votes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
