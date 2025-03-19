import grpc
import productM_pb2 as srv_msg
import productM_pb2_grpc as srv
import threading as mt
from requests import post

class ProductManager(srv.ProductManagerServicer):
    def __init__(self, num) -> None:
        self.laptop_queue = []
        self.num = num
        self.lock = mt.Lock()
        self.cv_prod = mt.Condition(self.lock)
        self.cv_cons = mt.Condition(self.lock)
        self.flask_addr = "localhost:8080"

    def send_to_flask(self, op, serial_number):
        flask_request = {
            "operation": op,
            "serial_number": serial_number
        }
        flask_response = post(url=self.flask_addr,json=flask_request)

    def Sell(self, request, context):
        with self.cv_prod:
            while len(self.laptop_queue) == self.num:
                self.cv_prod.wait()
            print(f"[Server] prodotto: {request.serial_number}")
            serial_number = request.serial_number
            self.laptop_queue.append(request.serial_number)
            self.cv_cons.notify()
        response = srv_msg.msg_ack(ack="ack")

        self.send_to_flask("sell", serial_number)
        return response


    def Buy(self, request, context):
        with self.cv_cons:
            while len(self.laptop_queue) == 0:
                self.cv_cons.wait()
            
            serial_number = self.laptop_queue.pop()
            self.cv_prod.notify()
        
        print(f"[Server] prelevato prodotto: {serial_number}")
        response = srv_msg.msg_sell(serial_number=serial_number)
        print(f"[SEVER - debug] buy - {serial_number}")
        self.send_to_flask("buy", serial_number)
        return response
