from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

POSTGRES_DATABASE_URL = 'postgresql://user:password@postgres/mydatabase'