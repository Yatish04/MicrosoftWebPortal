from flask import *
import pymongo
from bson import ObjectId

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
        
        res+="<td>"+str(cur["Name"])+"</td>"
        res+="<td>"+str(cur["Phone Number"])+"</td>"
        res+="<td>"+str(cur["Address"])+"</td>"
        res+="<td>"+str(cur["City"])+"</td>"
        res+="<td>"+str(cur["items"])+"</td>"
        res+="</tr>"

    return json.dumps({"status":200,"data":res})

@app.route('/ngo/myresources',methods=["GET"])
def get_db():
    uri = "mongodb://yatish:O7EsukGSyf4XSr1rCo3QaskijO5KA5VoX2lPps9KM8eJVxKUdEg1KdcxvIYs9R1QsYRIq8oNf6E1osIshY3E2A==@yatish.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(uri)
    db = client.Azure
    ref = db.ngo_data
    curr = ref.find_one({"_id":ObjectId("5bbdfe4a5c19951ceb09befe")})
    res={}
    res["data"] = curr["myresources"]
    return json.dumps(res)

@app.route('/ngo/myresources/update', methods=["POST"])
def updateones():
    uri = "mongodb://yatish:O7EsukGSyf4XSr1rCo3QaskijO5KA5VoX2lPps9KM8eJVxKUdEg1KdcxvIYs9R1QsYRIq8oNf6E1osIshY3E2A==@yatish.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(uri)
    db = client.Azure
    ref = db.ngo_data
    req = request.get_json()
    curr = ref.find_one({"_id":ObjectId("5bbdfe4a5c19951ceb09befe")})
    temp={}
    keys = req["name"]+'('+req["type"]+')'
    temp[keys] = req["qty"]
    if keys not in curr:
        curr["myresources"][keys] = req["qty"]
    else:
        curr["myresources"][keys] +=int(req["qty"])
    ref.update_one({"_id":ObjectId("5bbdfe4a5c19951ceb09befe")},{"$set":curr},upsert=False)
    return json.dumps({"status":"200"})

@app.route('/ngo/myresources/delete', methods=["POST"])
def deleteones():
    uri = "mongodb://yatish:O7EsukGSyf4XSr1rCo3QaskijO5KA5VoX2lPps9KM8eJVxKUdEg1KdcxvIYs9R1QsYRIq8oNf6E1osIshY3E2A==@yatish.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(uri)
    db = client.Azure
    ref = db.ngo_data
    ref = db.ngo_data
    req = request.get_json()
    curr = ref.find_one({"_id":ObjectId("5bbdfe4a5c19951ceb09befe")})
    temp={}
    keys = req["name"]+'('+req["type"]+')'
    temp[keys] = req["qty"]
    if keys not in curr["myresources"]:
        curr["myresources"][keys] = 0
    else:
        curr["myresources"][keys] = str(int(curr["myresources"][keys]) - int(req["qty"]))
        if int(curr["myresources"][keys]) <0:
            curr["myresources"][keys] = "0"
    ref.update_one({"_id":ObjectId("5bbdfe4a5c19951ceb09befe")},{"$set":curr},upsert=False)
    return json.dumps({"status":"200"})
