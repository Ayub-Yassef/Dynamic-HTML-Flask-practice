from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)
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

if __name__=="__main__":
    app.run(debug=True)