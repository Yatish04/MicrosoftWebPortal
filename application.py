from flask import *
import pymongo

app = Flask(__name__,template_folder=".")

@app.route("/",methods=["GET"])
def login():
    return render_template('index.html')

@app.route("/dashboard",methods=["GET"])
def dashboard():
    return render_template('dashboard.html')

@app.route('/ngo/resources',methods=['GET'])
def resources():
    # if "E-mail" not in session:
    #     return json.dumps({"status":500})
    uri = "mongodb://yatish:O7EsukGSyf4XSr1rCo3QaskijO5KA5VoX2lPps9KM8eJVxKUdEg1KdcxvIYs9R1QsYRIq8oNf6E1osIshY3E2A==@yatish.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(uri)
    db = client.Azure
    donate = db.resources
    res=""
    donated = donate.find()
    for cur in donated:
        res+="<tr>"
        for attr in cur:
            if attr == "_id":
                continue
            res+="<td>"+str(cur[attr])+"</td>"
        res+="</tr>"

    return json.dumps({"status":200,"data":res})