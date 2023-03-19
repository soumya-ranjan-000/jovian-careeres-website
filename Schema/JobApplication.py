from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()

class JobApplication(Base):
    __tablename__='Job_Application'
    Application_ID = Column(Integer,primary_key=True)
    jobid = Column(String)
    Name= Column(String)
    