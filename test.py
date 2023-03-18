import os
from dotenv import load_dotenv
import database as db

load_dotenv()

# print(os.getenv("db_pass"))
# print(os.getenv("db_username"))

job=db.getJobById("291222")
for i in job['Responsibilites'].split("\n"):
    print(i)
    