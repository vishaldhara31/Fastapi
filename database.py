from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 'postgresql://<username>:<password>@<ip_address/hostname>/' use this url
SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:god@localhost/fastapi'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Sessionlocal = sessionmaker(autocommit=False,autoflush=False,bind= engine)

Base = declarative_base()