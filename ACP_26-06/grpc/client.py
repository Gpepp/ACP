import grpc, sys
import productM_pb2 as srv_msg
import productM_pb2_grpc as srv
import threading as mt
from random import randint


def run_fun(address):
    casual = randint(0,200)
    with grpc.insecure_channel(target=address) as ch:
        stub = srv.ProductManagerStub(ch)
        if casual%2 == 0:
            serial_number = randint(0, 100)
            print(f"[Client] Sell: {serial_number}")
            response = stub.Sell(srv_msg.msg_sell(serial_number=serial_number))
            print(f"[Client] Risposta: {response}")
        else:
            print(f"[Client] Buy")
            response = stub.Buy(srv_msg.msg_buy())
    
            print(f"[Client] Risposta: {response.serial_number}")
    

if __name__ == "__main__":
    try:
        address = sys.argv[1]
    except IndexError:
        print("Insert valid host:port")
    

    ths = []
    for _ in range(10):
        th = mt.Thread(target=run_fun, args=(address,))
        th.start()
    

    for t in ths:
        t.join()