from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)
@app.route('/')
def create_profile():
    users=User.get_all_users()
    print(users)
    return render_template("read.html", users=users)

@app.route('/form_submission', methods=["POST"])
def profile_generated():
    data={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"]
    }
    User.add_user(data)
    return redirect("/")

@app.route('/create')
def members_display():
    return render_template("create.html")

if __name__=="__main__":
    app.run(debug=True)