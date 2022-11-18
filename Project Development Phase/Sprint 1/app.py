from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def signin():
    return render_template('signin.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')  

@app.route("/profile")
def profile():
    return render_template('profile.html')

@app.route("/home")
def home():
    return render_template("home.html")
