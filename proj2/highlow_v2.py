from flask import Flask, render_template, redirect, request, session, flash
import random
app = Flask(__name__)
app.secret_key = "hush its a secret"

@app.route('/')
def index():
    if 'message' not in session:
        session['message'] = ""
    if 'number' not in session:
        session['number'] = random.randint(1,101)
    return render_template("index.html", message = session['message'])

@app.route('/guess')
def guess():
    guess = int("")
    if guess == session['number']:
        session['message']="You Win!"
    if guess > session['number']:
        session['message']="Too high guess lower"
    elif guess < session['number']:
        session['message']="Too low guess higher"
    return redirect('/')

@app.route('/reset')
def reset():
    session['number']
    session.pop("number")
    session.pop("message")
    return redirect('/')
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
