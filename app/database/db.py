from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

engine = create_engine('postgresql://mrubio:secret@192.168.0.27:5432/hospederia')
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

