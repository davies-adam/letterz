from flask import Flask, render_template, redirect, url_for, send_from_directory
import json

app = Flask(__name__)

app.debug = True

@app.route("/")
def main():
    return render_template("main.html")