from sqlalchemy import create_engine,text
import os
from dotenv import load_dotenv

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
    stmt="SELECT * FROM jobs WHERE idjobs"
    with get_connection() as conn:
        result=conn.execute(text(f"SELECT * FROM jobs WHERE jobid={id}"))
        result_all=result.all()
        first_result=result_all[0]
    return first_result._asdict()    
    



   