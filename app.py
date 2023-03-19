from flask import Flask, render_template,jsonify,url_for,request,redirect
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
  sub_flag=request.args.get('sub_flag')
  return render_template('jobapplyform.html',job=job,flag=sub_flag)

@app.route("/job/apply/",methods=['POST'])
def getApplicantDetails():
  job_application={
    "job_id":request.form['jobid'],
    "name":request.form['name'],
    "email":request.form['email'],
    "experience":request.form['experience'],
    "linkedin":request.form['linkedin'],
    "expected_salary":request.form['salary']
  }
  flag=db.insert_job_application(job_application)
  if flag:
   return "<h1 style='color:green;'>Application Submitted Successfully.</h1>"
  else:
   return "<h1 style='color:red;'>There is some error occured while submitting your appliaction. Try again!!!</h1>"




if __name__ == "__main__":
  app.run(port='8080', debug=True)