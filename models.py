#Every models represented a table in our database
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.expression import null
from .database import Base

class Post(Base):
    __tablename__ = 'posts' #here we give the tablename that will show in the postgres 

    id = Column(Integer, primary_key = True, nullable= False)
    title = Column(String, nullable= False)
    content = Column(String, nullable= False)
    published = Column(Boolean, default=True)
