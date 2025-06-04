from database.db import Base
from sqlalchemy import Integer , Column , String


class User(Base):
    __tablename__ = "user"
    
    User_id = Column(Integer, primary_key=True )
    User_name = Column(String, index=True)
    Mobile = Column(String,index=True)
    Email = Column(String,index=True)
   
   