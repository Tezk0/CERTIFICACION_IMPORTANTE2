from flask import Flask, request, url_for, session, redirect, render_template
from usuarios import Usuario

app = Flask(__name__)

app.secret_key = "saflñdsfldkiijukiekswdx sfdafsafgrerjtretrt68545375473fefe432tewyp0o7ik7564utr4utj2jhg4"

@app.route("/")
def inicio():
    return render_template("index.html")

