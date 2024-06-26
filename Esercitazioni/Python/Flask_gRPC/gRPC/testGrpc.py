import sys, grpc

import statistics_pb2 as srv_msg
import statistics_pb2_grpc as srv


def run(port):
    
    ch = grpc.insecure_channel(f"127.0.0.1:{port}")
    stub = srv.statisticsStub(ch)
    mresponse = stub.getSensors(srv_msg.Empty())
if __name__ == "__main__":
    try:
        port = sys.argv[1]
    except IndexError:
        print("Insert Valid port")

    
    run(port=port)