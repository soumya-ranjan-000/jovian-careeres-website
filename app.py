from flask import Flask, render_template,jsonify

app = Flask(__name__)

JOBS=[
  {
    'id':1,
    'title': 'Data Analyst',
    'location':'Bangaluru, India',
    'salary':'Rs. 10,00,000'
  },
  {
    'id':2,
    'title': 'Data Engineer',
    'location':'Pune, India',
    'salary':'Rs. 40,00,000'
  },
  {
    'id':3,
    'title': 'Front-End Developer',
    'location':'Kochi, India'
  },
  {
    'id':4,
    'title': 'Back-End Developer',
    'location':'BBSR, India',
    'salary':'Rs. 19,00,000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS,company_name='Wipro')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(port='8080', debug=True)