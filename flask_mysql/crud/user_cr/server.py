from flask import Flask, render_template, request, redirect
from users import User
app - Flask(__name__)
@app.route('/')
def index():
    return redirect('/users')
@app.route('/users')
def users():
    return render_template("users.html", users=User.fetch_info())

if __name__=="__main__":
    app.run(debug=True)