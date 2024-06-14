from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgres://postgres:postgres@localhost:5442/pdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Stop(Base):
    __tablename__ = "stops"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    latitude = Column(String)
    longitude = Column(String)
    is_accessible = Column(Boolean, default=False)

    def __repr__(self):
        return f"Stop(id={self.id}, name={self.name}, latitude={self.latitude}, longitude={self.longitude})"


def create_all_tables():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
