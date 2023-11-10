from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Bengluru, IN',
        'salary': 'Rs. 10,00,000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Delhi, IN',
        'salary': 'Rs. 15,00,000'
    },
    {
        'id': 3,
        'title': 'FrontEnd Engineer',
        'location': 'Remote',
        'salary': 'Rs. 12,00,000'
    },
    {
        'id': 4,
        'title': 'BackEnd Engineer',
        'location': 'California, USA',
        'salary': '$ 120,000'
    }

]

@app.route('/')
def hello():
    return render_template('index.html', jobs=JOBS)

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)


if __name__=='__main__':
    app.run(debug=True)
