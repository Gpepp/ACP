import sys
import grpc
import productM_pb2 as srv_msg
import productM_pb2_grpc as srv






try:
    address = sys.argv[1]
except IndexError:
    print("Insert valid host:port")
        
with grpc.insecure_channel(address) as ch:
    stub = srv.ProductManagerStub(ch)
    response = stub.Sell(srv_msg.msg_sell(serial_number=10))
    print(response.ack)
    