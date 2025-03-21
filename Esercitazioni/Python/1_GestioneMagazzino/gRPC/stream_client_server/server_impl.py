import grpc
import magazzino_pb2 as mag_msg
import magazzino_pb2_grpc as mag
import logging as lg
from threading import Lock, Condition

class Maagazzino(mag.gestioneMagazzinoServicer):
    def __init__(self):
        self.laptop = []
        self.smartphone = []
        self.lock_smart = Lock()
        self.cv_smart_empty = Condition(self.lock_smart)
        self.lock_laptop = Lock()
        self.cv_laptop_empty = Condition(self.lock_laptop)

    def deposita(self, request, context):
        print(request.tipo, type(request.tipo))
        if request.tipo == 'laptop':
            with self.lock_laptop:

                lg.warning(f'Laptop id {request.id}')
                self.laptop.append(request.id)
                self.cv_laptop_empty.notify()
            
            response = mag_msg.msg_ack(ack=True)

        if request.tipo == 'smartphone':
            with self.lock_smart:

                lg.warning(f'Smartphone id {request.id}')
                self.smartphone.append(request.id)
                self.cv_smart_empty.notify()

            response = mag_msg.msg_ack(ack=True)

        else:
            lg.warning(f'Error tipo {request.tipo}')
            response = mag_msg.msg_ack(ack=False)
        
        lg.critical(f'\nlaptop: {self.laptop} \nsmartphone: {self.smartphone}')
        return response

    def preleva(self, request, context):
        if request.tipo == 'laptop':
            with self.cv_laptop_empty:
                while len(self.laptop) == 0:
                    lg.warning("Laptopt queue empty")
                    self.cv_laptop_empty.wait()
    
            art = self.laptop.pop()
            lg.warning(f'Laptop id {art}')
            response = mag_msg.articolo(tipo='laptop',id=art)

        if request.tipo == 'smartphone':
            with self.cv_smart_empty:
                while len(self.smartphone) == 0:
                    lg.warning("Smartphone queue empty")
                    self.cv_smart_empty.wait()

            art = self.smartphone.pop()
            lg.warning(f'Smartphone id {art}')
            response = mag_msg.articolo(tipo='smartphone',id=art)
        
        return response

    def show(self, request, context):
        if request.tipo == 'laptop':
            for el in self.laptop:
                art = mag_msg.articolo(tipo='laptop', id=el)
                yield art

        if request.tipo == 'smartphone':
            for el in self.smartphone:
                art = mag_msg.articolo(tipo='smartphone', id=el)
                yield art

    def add_multiple(self, requests, context):
        resp = []
        for req in requests:
            resp.append(self.deposita(req,context))
        
        for r in resp:
            yield r
