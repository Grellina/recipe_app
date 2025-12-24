from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


engine = create_engine('sqlite:///recipes.db', echo=True, future=True)      #соединение с БД


SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()