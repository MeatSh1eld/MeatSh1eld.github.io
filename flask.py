from flask import Flask, redirect, url_for, render_template, request
from threading import Thread

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/commands')
def commands():
    return render_template("commands.html")

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route('/<usr>')
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route('/discord')
def discord():
    return render_template("discord.html")

if __name__ == "__main__":
    app.run()


print('flask.py ready')