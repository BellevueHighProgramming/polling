from flask import Flask, render_template, request, redirect
import pollingDB
import json
from datetime import date

app = Flask(__name__)

validResourcePaths:set = {"page1/index.js", "page1/style.css", "page1/data.js"
                            "page2/index.js", "page2/style.css", "page2/data.js"}

@app.route('/')
def landingPage() -> str:
    # open file w/ questions, get question for today
    #question = json.load(open("questions.json", "r"))[date.today()]
    #return render_template('page1/index.html', question = question)
    return render_template('page1/index.html')
    

@app.route('/resource/<path:path>')
def resource(path: str) -> str:
    if path in validResourcePaths:
        resourceFile =  render_template(path)
    else:
        resourceFile =  render_template("noResource/noResource.html")
    
    return resourceFile

@app.route('/handle_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        type = request.args['type']
        if type == "question":
            return "How likely is 1+1 = 3"
        if type == "answers":
            return json.dumps({"A": "25%", "B": "50%", "C": "100%"})
                
    else:
        return render_template("noResource/noResource.html")
 



@app.route('/<path:path>')
def catchAll(path: str) -> redirect:
    return redirect("/")

app.run()
