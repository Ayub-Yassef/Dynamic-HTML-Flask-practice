from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def challenge_one():
    return render_template('index.html', message="Simply the Best", reps=2)

if __name__=="__main__":
    app.run(debug=True)