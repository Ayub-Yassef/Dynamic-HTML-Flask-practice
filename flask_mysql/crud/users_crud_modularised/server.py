from flask import Flask, render_template, request, redirect, app
# from user import User
from mysqlconnection import connectToMySQL
from flask_app import app

# app = Flask(__name__)
@app.route('/')
def create_profile():
    these_users=User.get_all_users()
    return render_template("read.html", users=these_users)#Users is a named argument. these_users is its value

@app.route('/application_process', methods=["POST"])
def application_process():
    User.add_user(request.form)
    return redirect("/")

@app.route('/application_page')
def application_page():
    return render_template("create.html")

@app.route('/users/update', methods=["POST"])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/users/update_user/<int:user_id>')
def update_user(user_id):
    # this_user=User.get_user(id)
    return render_template("update.html", user=User.get_user(user_id))

@app.route('/users/delete/<int:user_id>')
def delete(user_id):
    User.delete(user_id)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)