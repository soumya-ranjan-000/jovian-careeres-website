from sqlalchemy import create_engine,text,insert,Table,Column,MetaData,Integer,String
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from Schema.JobApplication import JobApplication

load_dotenv()

conn_url=f"mysql+pymysql://{os.getenv('db_username')}:{os.getenv('db_pass')}@ap-south.connect.psdb.cloud/joviandb?charset=utf8mb4"
ssl_args={
    'ssl_ca': "/etc/ssl/cert.pem"
}
engine = create_engine(conn_url,connect_args={
    "ssl":{
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})



def get_connection():
    return engine.connect()

def get_all_jobs():
    new_jobs=[]
    stmt="SELECT * FROM jobs;"
    with get_connection() as conn:
        for row in conn.execute(text(stmt)).all():
            new_jobs.append(row._asdict())
    return new_jobs

def getJobById(id):
    with get_connection() as conn:
        result=conn.execute(text(f"SELECT * FROM jobs WHERE jobid={id}"))
        result_all=result.all()
        first_result=result_all[0]
    return first_result._asdict()    

def insert_job_application(appliaction):
    metadata = MetaData()
    mytable = Table('Job_Application', metadata,
    Column('Application_ID', Integer, primary_key=True),
    Column('jobid', String),
    Column('Name', String),
    Column('Email',String),
    Column('Experience',String),
    Column('Linkedin',String),
    Column('Expected_Salary',Integer))
    with engine.connect() as conn:
        insert_query = mytable.insert().values(
            jobid=appliaction['job_id'],
            Name=appliaction['name'],
            Email=appliaction['email'],
            Experience=appliaction['experience'],
            Linkedin=appliaction['linkedin'],
            Expected_Salary=appliaction['expected_salary']
        )
        
        try:    
            result_proxy=conn.execute(insert_query)
            if result_proxy.rowcount > 0:
                print("Successfully inserted row")
                return True
            else:
                print("No rows were inserted")
                return False
        except Exception as e:
            print(e)
            return False 
    



   