from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://mrubio:secret@localhost:5432/hospederia')
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

