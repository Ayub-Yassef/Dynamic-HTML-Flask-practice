from flask import Flask, render_template, redirect, session, request
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/')
def survey_form():
    return render_template('index.html')

@app.route('/submit', methods = ["post"])
def result():
    session["Name"] = request.form["Name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["briefBio"] = request.form["briefBio"]
    return redirect('/form_submitted')

@app.route('/form_submitted')
def form_filled():
    return render_template('show.html')

if __name__=="__main__":
    app.run(debug=True)