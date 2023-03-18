from flask import Flask, render_template,jsonify,url_for
import database as db

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=db.get_all_jobs(),company_name='Wipro')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(get_jobs())

@app.route("/job/<id>")
def getJobDetails(id):
  job=db.getJobById(id)
  return render_template('job_details.html',job=job) 

@app.route("/api/job/<id>")
def jobsByIdAPI(id):
  job=db.getJobById(id)
  return jsonify(job) 

@app.route("/job/apply/<id>")
def applyForJob(id):
  job=db.getJobById(id)
  return render_template('jobapplyform.html',job=job)

if __name__ == "__main__":
  app.run(port='8080', debug=True)