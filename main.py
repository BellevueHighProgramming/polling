from flask import Flask, render_template, request, redirect
import pollingDB
import json
from datetime import date

app = Flask(__name__)

validResourcePaths:set = {"index/index.js", "index/style.css"}

@app.route('/')
def landingPage() -> str:
    # open file w/ questions, get question for today
    question = json.load(open("questions.json", "r"))[date.today()]
    return render_template('page1/index.html', question = question)
    

@app.route('/resource/<path:path>')
def resource(path: str) -> str:
    if path in validResourcePaths:
        return render_template(path)
    else:
        return render_template("noResource/noResource.html")
    
    return resourceFile


@app.route('/<path:path>')
def catchAll(path: str) -> redirect:
    return redirect("/")

app.run()
