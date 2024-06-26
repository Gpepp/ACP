import client_pb2 as srv_msg
import client_pb2_grpc as srv
import sys, grpc
from uuid import uuid4


if __name__ == "__main__":
    try:
        host = sys.argv[1]
    except IndexError:
        print("Specificare host:port")
    
    with grpc.insecure_channel(host) as ch:
        stub = srv.commandStub(ch)
        for i in range(10):
            if (i+1)%2:
                id = uuid4().hex
                msg = srv_msg.msg_deposita(id=id)
                response = stub.deposita(msg)
            else:
                msg = srv_msg.msg_preleva()
                response = stub.preleva(msg)
            

            print(f"risposta: {response}")
        