import magazzino_pb2 as srv_msg
import magazzino_pb2_grpc as srv
import sys, grpc

host = sys.argv[1]

with grpc.insecure_channel(host) as ch:
    stub = srv.magazzinoStub(ch)
    msg = srv_msg.msg_articolo(id='1', prod='laptop')
    response = stub.deposita(msg)
    print(response.ack)