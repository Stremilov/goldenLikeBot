from aiogram.types import CallbackQuery
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

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
    comments = relationship("Comment", back_populates="project")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey("videoproject.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    text = Column(Text, nullable=True)
    project = relationship("VideoProject", back_populates="comments")


class UserVote(Base):
    __tablename__ = "user_votes"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    voited = Column(Boolean, nullable=False, default=False)


def fill_video_projects():
    if session.query(VideoProject).count() == 0:
        projects = [
            VideoProject(name="Ни вчера, ни завтра", voices=0),
            VideoProject(name="Не убегай", voices=0),
            VideoProject(name="Дом", voices=0),
            VideoProject(name="Internal noise", voices=0),
            VideoProject(name="солл", voices=0),
            VideoProject(name="Чёрные мопсы", voices=0),
            VideoProject(name="Инсайт", voices=0),
            VideoProject(name="Доппельгангер", voices=0),
            VideoProject(name="slam casino - #XOXO", voices=0),
            VideoProject(name="Работа кинотеатров в годы Блокады", voices=0),
            VideoProject(name="ЯМЫ", voices=0),
        ]
        
        session.add_all(projects)
        session.commit()
