from sqlalchemy import create_engine,text
import os
conn_url=f"mysql+pymysql://{os.getenv('username')}:{os.getenv('pass')}@ap-south.connect.psdb.cloud/joviandb?charset=utf8mb4"
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

stmt="SELECT * FROM jobs;"
with get_connection() as conn:
    result=conn.execute(text(stmt))
    print(type(result))
    result_all=result.all()
    first_result=result_all[0]
    print(type(first_result),first_result._asdict())
    



   