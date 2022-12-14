from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


SQLALCHEMY_DATABASE_URL = "sqlite:///./student_base.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id_student = Column(Integer, primary_key=True, index=True)
    id_group = Column(Integer, )
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer, )
    birth_date = Column(String)
    login = Column(String)
    password = Column(String)


class Group(Base):
    __tablename__ = "group"

    id_group = Column(Integer, primary_key=True, index=True)
    name = Column(String)


SessionLocal = sessionmaker(autoflush=False, bind=engine)
