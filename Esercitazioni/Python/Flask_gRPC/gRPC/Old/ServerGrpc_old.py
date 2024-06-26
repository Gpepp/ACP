import grpc, time
import statistics_pb2 as srv_msg
import statistics_pb2_grpc as srv
from concurrent import futures

from pymongo import MongoClient


class ServerGrpc(srv.statisticsServicer):
    def __init__(self):
        self.db = MongoClient("mongodb://127.0.0.1/").get_database("sens")
        self.sensors_coll = self.db.get_collection("sensors")
    
    
    def getSensors(self, request, context):
        print("GetSensorActivate")
        sensors = self.sensors_coll.find({})
        for s in sensors:
            print(s)
            yield srv_msg.Sensor(id=s["_id"], data_type=s["data_type"])
    
    def getMean(self, request, context):
        type = self.sensors_coll.find({"_id":request.id})
        type_coll = self.db.get_collection(type+"_data")
        all_measure = type_coll.find({"sensor_id":request.id})
        med = 0
        num = 0
        for s in all_measure:
            med += s["data"]
            num +=1
        med = med/num

        return srv_msg.StringMessage(media=med)



if __name__ == "__main__":
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    srv.add_statisticsServicer_to_server(ServerGrpc,server=server)
    port = server.add_insecure_port("127.0.0.1:0")

    server.start()

    print("server start: " + str(port))

    server.wait_for_termination()