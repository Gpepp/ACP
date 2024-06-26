import client_pb2 as srv_msg
import client_pb2_grpc as srv
import grpc, sys


host = sys.argv[1]
print(host)

with grpc.insecure_channel(host) as ch:
    stub = srv.commandStub(ch)
    #response = stub.deposita(srv_msg.msg_deposita(id='1'))
    response = stub.preleva(srv_msg.msg_preleva())
    print(response.response)