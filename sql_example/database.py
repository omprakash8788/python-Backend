from sqlalchemy.orm import DeclarativeBase
class Base(DeclarativeBase):
    pass

from sqlalchemy.orm import(
    Mapped,
    mapped_column
)

class User(Base):
    __tablename__="user"
    id:Mapped[int]=mapped_column(
        primary_key=True,
    )
    name:Mapped[str]
    email:Mapped[str]

DATABASE_URL = "sqlite:///./test.db"

from sqlalchemy import create_engine
engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

# A session in SQLAlchemy 

from sqlalchemy.orm import sessionmaker
SessionLocal = sessionmaker(
 autocommit=False, autoflush=False, bind=engine
)