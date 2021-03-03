from flask import Flask,render_template,redirect,request,session,make_response,url_for,render_template_string
import pickle
import io
import sys
import base64
import os

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("login"))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.form.get("Username"):
        Username = request.form.get("Username")
        html = "<p>Hello %s</p>" % Username
        return render_template_string(html)
    else:
        return render_template("login.html")
        
if __name__ == "__main__":
    app.run("0.0.0.0")
