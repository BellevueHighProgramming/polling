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
    name = request.cookies.get('enteredData')
    if(name == "true"):
        return render_template('page2/index.html')
    return render_template('page1/index.html')
    

@app.route('/resource/<path:path>')
def resource(path: str) -> str:
    if path in validResourcePaths:
        resourceFile =  render_template(path)
    else:
        resourceFile =  render_template("noResource/noResource.html")
    
    return resourceFile

@app.route('/api', methods=['GET'])
def api():
    if request.method == 'GET':
        type = request.args['type']
        if type == "question":
            return "How likely is 1+1 = 3"
        elif type == "answers":
            return json.dumps({"A": "Tetris", "B": "Beer", "C": "Chicken"})
        elif type == "pollingType":
            #Calling pollingDB to obtain polling data
            return json.dumps({"A": "25%", "B": "50%", "C": "10%"})

        
    elif request.method == 'POST':
        type = request.args['type']
        if type == "result":
            data = request.args['data']   
            #Call pollingDB to handle data
    
                
    else:
        return render_template("noResource/noResource.html")
 



@app.route('/<path:path>')
def catchAll(path: str) -> redirect:
    return redirect("/")

app.run()
