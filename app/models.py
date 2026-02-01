#Every models represented a table in our database
#sqlalchemy doesnt ment to make migration(making changes in the table) in our table we have to use different software
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .database import Base

class Post(Base):
    __tablename__ = 'posts' #here we give the tablename that will show in the postgres 

    id = Column(Integer, primary_key = True, nullable= False)
    title = Column(String, nullable= False)
    content = Column(String, nullable= False)
    published = Column(Boolean, nullable= False, server_default= 'TRUE')
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default= text('now()'))
