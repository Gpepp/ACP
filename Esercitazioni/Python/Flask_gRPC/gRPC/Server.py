import grpc

from concurrent import futures

import statistics_pb2 as srv_msg
import statistics_pb2_grpc as srv

from pymongo import MongoClient

def getDb():
    return MongoClient("mongodb://127.0.0.1").get_database('sens')

class ServerStatistics(srv.statisticsServicer):
    def __init__(self, db):
        self.db = db
    
    def getSensors(self, request, context):
        print("GetSensorCall")
    
    def getMean(self, request, context):
        print("GetSensorCall")
        
    

if __name__ == "__main__":
    db = getDb()

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=(('grpc.so_reuseport', 0),))
    srv.add_statisticsServicer_to_server(ServerStatistics(db=db),server=server)
    
    port = server.add_insecure_port("127.0.0.1:0")
    print(f"Server start at port: {port}")
    
    server.start()

    server.wait_for_termination()