from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    return redirect ('/users')

@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all_users())

@app.route('/user/add_new')
def add_new():
    return render_template("add_new.html")

@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.add_user(request.form)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show(id):
    user = User.get_user(id)
    return render_template("show_user.html", user=user)

@app.route('/user/edit_user/<int:id>')
def edit(id):
    return render_template("edit_user.html", user=User.get_user(id))

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    User.destroy(id)
    return redirect('/users')






























# def add_nums():
#     return [1,2,3,4,5]
# print(add_nums())