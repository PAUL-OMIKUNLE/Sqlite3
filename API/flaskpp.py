#!/usr/bin/env python3
from flask import Flask, jsonify, render_template, request 
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("./index.html")


@app.route('/compute')
def compute():
    a = 4
    b = 3
    return str(a * b)


@app.route('/result')
def name_result():
    name = {
        "first": "Paul",
        "last": "Omikunle",
        "course": "Data Science"
    }
    {
        "first": "Lola",
        "last": "Omikunle",
        "course": "Machine learning"
    }
    return jsonify(name)


@app.route('/score', methods= ["POST"])
def score_val():
    DataDict = request.get_json()

    return jsonify(DataDict)



if __name__=='__main__':
    app.run(debug=True)
