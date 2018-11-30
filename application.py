from flask import *
import pymongo
from bson import ObjectId

app = Flask(__name__,template_folder=".")

@app.route("/",methods=["GET"])
@app.route("/home",methods=["GET"])
def login():
    return render_template('index.html')

@app.route("/dashboard",methods=["GET"])
def dashboard():
    return render_template('dashboard.html')

@app.route("/weather/dashboard",methods=["GET"])
def renderdash():
    return render_template('dashboard_weather.html')

@app.route("/relief/home",methods=["GET"])
def renderrelief():
    return render_template('relief.html')

@app.route('/ngo/resources',methods=['GET'])
def resources():

    # if "E-mail" not in session:
    #     return json.dumps({"status":500})
    uri = "mongodb://yatishhr:pXYRVwZL2myXglrdgLSwAVKUb5U8AnbN1m83JXogbpKXlmwBBOdk4Py6s7EgBGsJoWRvTFJ6o7nNDY1n99HHMw==@yatishhr.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(uri)
    db = client.Azure
    donate = db.resources
    res=""
    donated = donate.find()
    for cur in donated:
        res+="<tr>"

        res+="<td>"+str(cur["Name"])+"</td>"
        res+="<td>"+str(cur["phone_number"])+"</td>"
        res+="<td>"+str(cur["Address"])+"</td>"
        res+="<td>"+str(cur["City"])+"</td>"
        res+="<td>"+str(cur["items"])+"</td>"
        res+="</tr>"

    return json.dumps({"status":200,"data":res})

@app.route('/ngo/myresources',methods=["GET"])
def get_db():
    uri = "mongodb://yatishhr:pXYRVwZL2myXglrdgLSwAVKUb5U8AnbN1m83JXogbpKXlmwBBOdk4Py6s7EgBGsJoWRvTFJ6o7nNDY1n99HHMw==@yatishhr.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(uri)
    db = client.Azure
    ref = db.ngo_data
    curr = ref.find_one({"_id":ObjectId("5c017a385c19953eb9a0497c")})
    res={}
    res["data"] = curr["myresources"]
    return json.dumps(res)

@app.route('/ngo/myresources/update', methods=["POST"])
def updateones():
    uri = "mongodb://yatishhr:pXYRVwZL2myXglrdgLSwAVKUb5U8AnbN1m83JXogbpKXlmwBBOdk4Py6s7EgBGsJoWRvTFJ6o7nNDY1n99HHMw==@yatishhr.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(uri)
    db = client.Azure
    ref = db.ngo_data
    req = request.get_json()
    curr = ref.find_one({"_id":ObjectId("5c017a385c19953eb9a0497c")})
    temp={}
    keys = req["name"]+'('+req["type"]+')'
    temp[keys] = req["qty"]
    if keys not in curr["myresources"]:
        curr["myresources"][keys] = req["qty"]
    else:
        temp = int(curr["myresources"][keys])
        curr["myresources"][keys] = str(temp+int(req["qty"]))
    ref.update_one({"_id":ObjectId("5c017a385c19953eb9a0497c")},{"$set":curr},upsert=False)
    return json.dumps({"status":"200"})

@app.route('/ngo/myresources/delete', methods=["POST"])
def deleteones():
    uri = "mongodb://yatishhr:pXYRVwZL2myXglrdgLSwAVKUb5U8AnbN1m83JXogbpKXlmwBBOdk4Py6s7EgBGsJoWRvTFJ6o7nNDY1n99HHMw==@yatishhr.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(uri)
    db = client.Azure
    ref = db.ngo_data
    ref = db.ngo_data
    req = request.get_json()
    curr = ref.find_one({"_id":ObjectId("5c017a385c19953eb9a0497c")})
    temp={}
    keys = req["name"]+'('+req["type"]+')'
    temp[keys] = req["qty"]
    if keys not in curr["myresources"]:
        curr["myresources"][keys] = "0"
    else:
        curr["myresources"][keys] = str(int(curr["myresources"][keys]) - int(req["qty"]))
        if int(curr["myresources"][keys]) <0:
            # curr["myresources"][keys] = "0"
            del curr["myresources"][keys]
    ref.update_one({"_id":"0"},{"$set":curr},upsert=False)
    return json.dumps({"status":"200"})

@app.route('/relief/<disaster_id>/getassets',methods=["GET"])
def getassets(disaster_id):
    uri = "mongodb://yatishhr:pXYRVwZL2myXglrdgLSwAVKUb5U8AnbN1m83JXogbpKXlmwBBOdk4Py6s7EgBGsJoWRvTFJ6o7nNDY1n99HHMw==@yatishhr.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
    client = pymongo.MongoClient(uri)
    db = client.Azure
    ref = db.Victim
    cursor = ref.find_one({"user_id":"0","Disasterid":disaster_id})
    res={}
    res["src"] = cursor["facial"]
    res["analytics"]=cursor["victims"]
    res["status"] = 200
    return json.dumps(res)
