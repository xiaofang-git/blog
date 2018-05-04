from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, Text, Time
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:密码@ip地址:3306/blog', echo=True)
Session = sessionmaker(bind=engine)


class blog(Base):
    __tablename__ = "blog"
    id = Column(Integer(), primary_key=True)
    title = Column(String(50))
    absc = Column(String(50))
    context = Column(String(50))
    ptime = Column(Time())


session = Session()
b = blog(title="自信", absc="自信的力量")
session.add(b)
session.commit()