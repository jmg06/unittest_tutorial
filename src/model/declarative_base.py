from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a new SQLite database
engine = create_engine("sqlite:///db.sqlite")
# Session class allow us to comunicate with the database
Session = sessionmaker(bind=engine)

# Base class to create models
Base = declarative_base()
# Create a session object
session = Session()
