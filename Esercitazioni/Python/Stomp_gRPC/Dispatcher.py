import magazzino_pb2 as srv_msg
import magazzino_pb2_grpc as srv

import multiprocess as mp
import sys, grpc, time, stomp
from concurrent import futures



def run_proc(msg, MOM, grpc_host):
    print("Process Start...")
    msg = msg.split('-')
    print(msg)
    with grpc.insecure_channel(grpc_host) as ch:
        stub = srv.magazzinoStub(ch)
        response = "error"
        if msg[0] == 'deposita':
            msgRe = srv_msg.msg_articolo(id = msg[2], prod = msg[1])
            response = stub.deposita(msgRe)
            response = response.ack
        if msg[0] == 'preleva':
            msgRe = srv_msg.msg()
            response = stub.preleva(msgRe)
            response = '-'.join([response.id, response.prod])
        
        if msg[0] == 'svuota':
            msgRe = srv_msg.msg()
            response = stub.svuota(msgRe)
            response = response.ack
        
        MOM.send("/queue/response", response)

class Listener(stomp.ConnectionListener):
    def __init__(self, MOM, grpc_host):
        self.MOM = MOM
        self.grpc_host = grpc_host

    def on_message(self, frame):
        proc = mp.Process(target=run_proc, args=(frame.body, self.MOM, self.grpc_host))
        proc.start()

if __name__ =="__main__":
    try:
        host = sys.argv[1]
    except IndexError:
        print("Insert host:port")

    
    conn = stomp.Connection([("localhost","61613")])
    conn.set_listener("", Listener(conn,host))
    conn.connect()

    conn.subscribe('/queue/requests', id = 1)


    time.sleep(20000)
    