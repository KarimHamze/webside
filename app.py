from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengaluru - India',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Dehli - India',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'Frontend Engenieer',
        'location': 'Remote',
    },
    {
        'id': 4,
        'title': 'Backend Engenieer',
        'location': 'San Francisco - USA',
        'salary': '$120,000'
    },
]


@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=jobs, company_name='Jovian')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
