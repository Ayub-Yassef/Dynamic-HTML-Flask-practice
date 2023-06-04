from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = "deny, deny, deny"
@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 1
    return render_template("index.html")
@app.route('/reset')
def reset_counter():
    session.clear()
    return redirect('/')
if __name__=="__main__":
    app.run(debug=True)