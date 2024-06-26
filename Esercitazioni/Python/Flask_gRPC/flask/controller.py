from flask import Flask, request
from pymongo import mongo_client

db = mongo_client.MongoClient("mongodb://127.0.0.1/").get_database("sens")


Controller = Flask(__name__)

accepted_data_type = ["press", "temp"]


@Controller.post("/sensor")
def sensor():
    data = request.get_json()
    coll = db.get_collection("sensors")
    try:
        coll.insert_one(data)
    except :
        return {"result":"error dbError"}
    return {"result":"success"}
    

@Controller.post("/data/<data_type>")
def rilev(data_type):
    data = request.get_json()
    if data_type in accepted_data_type:
        coll = db.get_collection(data_type+"_data")
        coll.insert_one(data)
    else:
        print("invalid: ",data_type =="press")
        return {"result":"error - Datatype invalid"} 
    
    return {"result":"success"}

if __name__ == "__main__":
    Controller.run(port=8080, debug=True)