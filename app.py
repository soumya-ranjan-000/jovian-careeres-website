from flask import Flask, render_template,jsonify
from database import get_connection
from sqlalchemy import text

app = Flask(__name__)

def get_jobs():
  new_jobs=[]
  stmt="SELECT * FROM jobs;"
  with get_connection() as conn:
    for row in conn.execute(text(stmt)).all():
        new_jobs.append(row._asdict())
  return new_jobs

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=get_jobs(),company_name='Deloitte')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(get_jobs())

if __name__ == "__main__":
  app.run(port='8080', debug=True)