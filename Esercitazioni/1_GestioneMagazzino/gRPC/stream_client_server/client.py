import logging as lg
import sys
import grpc
from random import randint
import magazzino_pb2 as mag_msg
import magazzino_pb2_grpc as mag
import threading as mt


def start(socket, n):
    lg.warning("Thread start")
    with grpc.insecure_channel(socket) as ch:
        stub = mag.gestioneMagazzinoStub(ch)
        if n == 'pl':
            resposne = stub.preleva(mag_msg.msg_tipo(tipo='laptop'))
            print("[CLIENT] LAPTOP PRELEVATO: ", resposne.id , ' ', resposne.tipo)
        
        if n == 'ps':
            resposne = stub.preleva(mag_msg.msg_tipo(tipo='smartphone'))
            print("[CLIENT] SMARTPHONE PRELEVATO: ", resposne.id , ' ', resposne.tipo)
        
        if n == 'dl':
            id = randint(0,100)
            resposne = stub.deposita(mag_msg.articolo(tipo='laptop',id=id))
            print(f"[CLIENT] LAPTOPO DEPOSITATO: {resposne}")
        
        if n == 'ds':
            id = randint(0,100)
            resposne = stub.deposita(mag_msg.articolo(tipo='smartphone',id=id))
            print("[CLIENT] SMARTPHONE DEPOSITATO: ", resposne)
        if n == 'st-s':
            products = stub.show(mag_msg.msg_tipo(tipo="smartphone"))
            for product in products:
                print(product)
        if n == 'st-l':
            products = stub.show(mag_msg.msg_tipo(tipo="laptop"))
            for product in products:
                print(product)
        if n == 'm':
            products_to_add = []
            for i in range(0,5):
                id = randint(0,100)
                if i%2 == 0:
                    products_to_add.append(mag_msg.msg_articolo(tipo='laptop', id=id))

                else:
                    products_to_add.append(mag_msg.msg_articolo(tipo='smartphone', id=id))

            for prduct in products_to_add:
                yield 

if __name__=="__main__":

    ip = sys.argv[1]
    
    print(ip)

    while True:
        choise = input("deposita o preleva (pl - ps - dl - ds - st-s - st-l)")
        start(ip, choise)
